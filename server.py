from flask import Flask, request, jsonify, render_template
import sqlite3
from textblob import TextBlob
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)
gemini_model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('mood_tracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS moods
                 (user_id TEXT, mood TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS journal
                 (user_id TEXT, entry TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

init_db()

# System prompt for Gemini to align with problem statement
SYSTEM_PROMPT = """
You are CalmBot, an AI companion designed to help users heal from emotional distress and unresolved trauma, often rooted in childhood wounds. Your goal is to empower users to recognize, monitor, and heal deep-rooted emotional wounds, guiding them toward inner peace amidst external chaos. For every response:
- Acknowledge the user's emotion (e.g., happiness, sadness, anger, anxiety) empathetically.
- Recognize potential trauma, such as childhood hurts, neglect, or avoidance patterns, without assuming specifics.
- Use motivational, uplifting language to inspire resilience and hope (e.g., 'You're stronger than the scars you carry').
- Suggest personalized actions like journaling, breathing exercises, or visiting the Serenity Garden to find calm.
- Keep responses concise (100-150 words), empathetic, and aligned with fostering peace with oneself.
- Avoid generic or overly clinical tones; be warm and human-like.
"""

def generate_gemini_response(prompt, user_input):
    try:
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser input: {user_input}\n\nRespond appropriately."
        response = gemini_model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        print(f"Gemini API error: {e}")
        # Fallback to TextBlob
        analysis = TextBlob(user_input)
        sentiment = 'positive' if analysis.sentiment.polarity > 0 else 'negative' if analysis.sentiment.polarity < 0 else 'neutral'
        return f"I hear you. Your input feels {sentiment}. Want to explore this with a journal entry or a breathing exercise?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mood/<mood>', methods=['POST'])
def log_mood(mood):
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID required'}), 400
    conn = sqlite3.connect('mood_tracker.db')
    c = conn.cursor()
    c.execute("INSERT INTO moods (user_id, mood) VALUES (?, ?)", (user_id, mood))
    conn.commit()
    conn.close()
    # Use Gemini for dynamic response
    response_text = generate_gemini_response(
        f"User is feeling {mood}.",
        f"I'm feeling {mood} today."
    )
    return jsonify({'response': response_text})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')
    user_id = data.get('user_id')
    if not message or not user_id:
        return jsonify({'error': 'Message and user ID required'}), 400
    # Use Gemini for chat response
    response_text = generate_gemini_response(
        "User is chatting with CalmBot.",
        message
    )
    return jsonify({'response': response_text})

@app.route('/journal', methods=['POST'])
def save_journal():
    data = request.get_json()
    user_id = data.get('user_id')
    entry = data.get('entry')
    if not user_id or not entry:
        return jsonify({'error': 'User ID and entry required'}), 400
    conn = sqlite3.connect('mood_tracker.db')
    c = conn.cursor()
    c.execute("INSERT INTO journal (user_id, entry) VALUES (?, ?)", (user_id, entry))
    conn.commit()
    conn.close()
    # Analyze journal entry with Gemini
    response_text = generate_gemini_response(
        "User submitted a journal entry.",
        f"Journal entry: {entry}"
    )
    return jsonify({'response': response_text})

@app.route('/progress', methods=['POST'])
def get_progress():
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID required'}), 400
    conn = sqlite3.connect('mood_tracker.db')
    c = conn.cursor()
    c.execute("SELECT mood, COUNT(*) FROM moods WHERE user_id = ? GROUP BY mood", (user_id,))
    results = c.fetchall()
    conn.close()
    emotions = [row[0] for row in results]
    counts = [row[1] for row in results]
    summary = f"You've logged {sum(counts)} moods: {', '.join([f'{e} ({c})' for e, c in zip(emotions, counts)])}."
    return jsonify({'emotions': emotions, 'counts': counts, 'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)