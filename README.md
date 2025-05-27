CalmBot: Your Companion for Inner Peace
 
CalmBot is an AI-powered emotional support platform designed to help users heal from unresolved trauma and find peace amidst life’s chaos. Built for the Peace with Oneself problem statement at Hackathon 2025, CalmBot empowers individuals to recognize, monitor, and mend deep-rooted emotional wounds, often stemming from childhood hurts or societal neglect. Whether you’re feeling happy, sad, angry, or anxious, CalmBot offers empathetic guidance, personalized actions, and a safe space to reflect, fostering resilience and self-compassion.
Accessible via a responsive website and a Telegram bot, CalmBot ensures users can seek support anytime, anywhere. Powered by Google’s Gemini model and a custom learning model with adaptive memory, CalmBot delivers trauma-aware responses and grows smarter by learning from user interactions. Join us in creating a world where inner peace is within everyone’s reach.
Problem Statement: Peace with Oneself
The Peace with Oneself challenge calls for solutions to help individuals heal from emotional distress and unresolved trauma, which often originate in childhood and are exacerbated by external chaos. CalmBot addresses this by:

Acknowledging Trauma: Recognizes potential wounds (e.g., neglect, betrayal) with empathy, validating users’ emotions.
Empowering Healing: Offers actionable steps like journaling, breathing exercises, and mindfulness to process pain.
Building Resilience: Motivates users to break cycles of avoidance and find strength in their journey.
Creating Calm: Provides tools like the Serenity Garden and chat support to anchor users in peace.

CalmBot is more than a tool—it’s a companion for those seeking to reclaim their emotional well-being and thrive.
Features

Emotion-Based Support: Choose from Happy, Sad, Angry, or Anxious to receive tailored, empathetic responses that address trauma and suggest healing actions.
Serenity Garden: A virtual space to plant flowers, accompanied by soothing bird and forest sounds, promoting mindfulness and calm.
Journaling: Reflect on emotions with guided prompts, storing entries securely to track your healing journey.
Breathing Exercises: Guided 4-4-8 breathing to reduce stress and ground users in the present.
Your Emotional Journey: Visualize mood trends with a bar chart, celebrating progress in emotional awareness.
Chat Mode: Engage in freeform conversations via the website or Telegram bot, with responses that adapt to your emotional state.
Dual AI Models:
Gemini Model: Powers empathetic, trauma-aware responses for real-time support.
Custom Learning Model: Learns from unknown inputs by asking for clarification, storing new knowledge in memory for future interactions.


Multi-Platform Access:
Website: A beautifully designed, responsive interface for immersive support.
Telegram Bot: Instant access via social platforms, perfect for on-the-go users.


Mental Health Resources: Links to trusted services like BetterHelp and Crisis Text Line for additional support.

Tech Stack
Backend

Python: Core language for server and bot logic.
Flask: Lightweight web framework for the CalmBot website.
SQLite: Database for storing user moods, journal entries, and chat history.
Google Generative AI (Gemini): Powers dynamic, empathetic responses.
TextBlob: Fallback for sentiment analysis when Gemini is unavailable.
python-telegram-bot: Handles Telegram bot interactions.

Frontend

HTML5/CSS3: Responsive website design with Tailwind CSS for styling.
JavaScript: Client-side interactivity, powered by p5.js for Serenity Garden visuals.
Tailwind CSS: Utility-first CSS for a modern, gradient-based UI.
Google Fonts (Poppins): Clean typography for a welcoming feel.

Tools & APIs

Gemini API: For trauma-aware, motivational responses.
Telegram API: Enables bot functionality on social platforms.
python-dotenv: Manages environment variables (e.g., API keys).
Freesound.org: CC0-licensed bird and forest sounds for Serenity Garden.

Infrastructure

GitHub: Version control and collaboration.
Windows (Local): Development environment (e.g., C:\Users\dell\calm).
SQLite Database: Lightweight storage for user data.

How It Works

Access CalmBot:

Visit the website at http://localhost:5000 (or deployed URL).
Interact via Telegram by searching for @YourCalmBot.


Select Your Mood:

Click Happy, Sad, Angry, or Anxious on the website or Telegram buttons.
Receive a Gemini-powered response acknowledging potential trauma and suggesting actions (e.g., “Your sadness is valid… Try journaling to let it out.”).


Engage with Features:

Serenity Garden: Plant mood-colored flowers with calming audio.
Journal: Answer prompts to reflect and heal.
Breathing: Follow guided exercises to reduce stress.
Chat: Use /chat on Telegram or the website’s chatbox for freeform support.


Adaptive Learning:

If CalmBot doesn’t understand an input (e.g., “xyz”), it asks, “Tell me what you mean by that.”
Stores clarifications in memory (unknown_inputs.json), improving future responses.


Track Progress:

View mood trends in “Your Emotional Journey” on the website.
All interactions are logged securely in SQLite for personalized insights.



Installation

Clone the Repository:
git clone https://github.com/yourusername/calmbot.git
cd calmbot


Install Dependencies:
pip install flask python-telegram-bot google-generativeai python-dotenv textblob
python -m textblob.download_corpora


Set Up Environment:

Create .env in calmbot/:TELEGRAM_TOKEN=your_telegram_token
GOOGLE_API_KEY=your_gemini_api_key


Place index.html in calmbot/templates/.
Place audio files (e.g., bird_sounds.mp3) in calmbot/static/.


Run the Website:
python server.py


Access at http://localhost:5000.


Run the Telegram Bot:
python calmbot.py


Interact via Telegram (@YourCalmBot).


Database:

SQLite database (mood_tracker.db) is created automatically.
Stores moods, journal entries, and chat history.



Usage

Website:

Navigate to the homepage, select a mood, and explore features like Serenity Garden or journaling.
Use the chatbox for real-time support.
View your emotional progress in “Your Emotional Journey.”


Telegram Bot:

Start with /start to see mood buttons.
Use /chat for freeform conversations.
Responses adapt based on your input and history.


Example Interaction:

User: “I’m feeling stressed.”
CalmBot: “Stress can feel so heavy, often tied to life’s chaos or past worries. Try a 4-4-8 breathing exercise: inhale for 4, hold for 4, exhale for 8. Want to share more? I’m here.”
User: “xyz”
CalmBot: “I don’t know what you mean by ‘xyz,’ but I’ll learn! Can you explain it? Let’s keep chatting.”



Why CalmBot?
CalmBot stands out by:

Trauma-Aware Design: Aligns with Peace with Oneself, addressing childhood wounds and societal noise with empathy.
Dual AI Approach: Combines Gemini’s robustness with a custom model that learns from users, ensuring personalized support.
Accessible Platforms: Website and Telegram bot make emotional care available 24/7.
Holistic Healing: Integrates mindfulness (Serenity Garden, breathing), reflection (journaling), and motivation (chat) for comprehensive support.
Privacy-First: Stores data locally in SQLite, prioritizing user trust.

Future Enhancements

Mobile App: Develop iOS/Android apps for broader access.
Advanced Learning: Train the custom model on user data for deeper personalization.
Multilingual Support: Add languages to reach diverse communities.
Wearable Integration: Sync with devices to monitor stress and suggest real-time interventions.
Community Features: Create a safe space for users to share stories and support each other.

Contributing
We welcome contributions! To get started:

Fork the repository.
Create a branch: git checkout -b feature/your-feature.
Commit changes: git commit -m "Add your feature".
Push: git push origin feature/your-feature.
Open a pull request.

Please follow our Code of Conduct and report issues via GitHub Issues.
License
This project is licensed under the MIT License. See LICENSE for details.
Team
Built with ❤️ by [Your Team Name] for Hackathon 2025. We’re passionate about mental health, AI, and creating solutions that empower healing.

Contact: support@calmbot.com
GitHub: yourusername
Telegram: @YourCalmBot

Acknowledgments

Hackathon 2025: For inspiring us to tackle Peace with Oneself.
Google Gemini: For powering empathetic AI responses.
Freesound.org: For CC0 audio enhancing the Serenity Garden.
Open Source Community: For tools like Flask, p5.js, and python-telegram-bot.


Let’s heal, grow, and find peace together with CalmBot. 🌱
