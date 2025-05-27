# CalmBot: Your Companion for Inner Peace 🌱


**CalmBot** is an AI-powered emotional support platform designed to help users heal from unresolved trauma and find peace amid life’s chaos. Created for the **Peace with Oneself** challenge at Hackathon 2025, CalmBot helps individuals recognize, monitor, and begin to mend deep emotional wounds that often trace back to childhood pain or societal neglect.

Whether you're feeling happy, sad, angry, or anxious, CalmBot offers empathetic guidance, personalized actions, and a safe space for reflection. It supports your journey by fostering resilience and self-compassion.

Accessible through a responsive website and a Telegram bot, CalmBot gives users access to support anytime and anywhere. Powered by Google’s Gemini model and a custom learning system with adaptive memory, it responds with emotional awareness and continuously grows smarter from each interaction.

## 🧠 Problem Statement: Peace with Oneself

The **Peace with Oneself** challenge calls for solutions to help individuals heal from emotional distress and unresolved trauma, which often originate in childhood and are exacerbated by external chaos. CalmBot addresses this by:

- **Acknowledging Trauma:** Recognizes potential wounds (e.g., neglect, betrayal) with empathy, validating users’ emotions.
- **Empowering Healing:** Offers actionable steps like journaling, breathing exercises, and mindfulness to process pain.
- **Building Resilience:** Motivates users to break cycles of avoidance and find strength in their journey.
- **Creating Calm:** Provides tools like the Serenity Garden and chat support to anchor users in peace.

CalmBot is more than a tool—it’s a companion for those seeking to reclaim their emotional well-being and thrive.

---

## 🌟 Features

- **Emotion-Based Support:** Choose from *Happy*, *Sad*, *Angry*, or *Anxious* to receive tailored, empathetic responses that address trauma and suggest healing actions.
**Serenity Garden:** A virtual space where you can plant flowers and listen to soothing bird and forest sounds to promote mindfulness and calm.
- **Journaling:** Reflect on emotions with guided prompts, storing entries securely to track your healing journey.
- **Breathing Exercises:** Guided 4-4-8 breathing to reduce stress and ground users in the present.
- **Your Emotional Journey:** Visualize mood trends with a bar chart, celebrating progress in emotional awareness.
- **Chat Mode:** Engage in freeform conversations via the website or Telegram bot, with responses that adapt to your emotional state.

### Dual AI Models
- **Gemini Model:** Powers empathetic, trauma-aware responses for real-time support.
- **Custom Learning Model:** Learns from unknown inputs by asking for clarification, storing new knowledge for future interactions.

### Multi-Platform Access
- **Website:** Beautiful, responsive design for immersive support.
- **Telegram Bot:** Instant access via social platforms, perfect for on-the-go users.

### Mental Health Resources
- Links to trusted services like BetterHelp and Crisis Text Line for additional support.

---

## 🛠 Tech Stack

### Backend
- **Python**
- **Flask**
- **SQLite**
- **Google Generative AI (Gemini)**
- **TextBlob**
- **python-telegram-bot**

### Frontend
- **HTML5/CSS3**
- **JavaScript**
- **Tailwind CSS**
- **Google Fonts (Poppins)**
- **p5.js**

### Tools & APIs
- **Gemini API**
- **Telegram API**
- **python-dotenv**
- **Freesound.org** (bird and forest sounds)

### Infrastructure
- **GitHub**
- **Local Windows Dev**
- **SQLite Database**

---

## 🔍 How It Works

### Access CalmBot
- Website: [http://localhost:5000](http://localhost:5000)
- Telegram: Search for `@calm56bot`
- Video link: https://drive.google.com/file/d/1cK67B3pFBr6WiDn-L-hdvR1b_41KU7x7/view?usp=sharing

### Select Your Mood
Click *Happy*, *Sad*, *Angry*, or *Anxious* to receive a Gemini-powered response.

### Engage with Features
- **Serenity Garden:** Plant flowers and enjoy ambient sounds.
- **Journal:** Reflect on guided prompts.
- **Breathing:** Try calming breathing exercises.
- **Chat:** Use `/chat` on Telegram or the website chatbox.

### Adaptive Learning
- CalmBot asks for clarification when it encounters unknown inputs.
- Stores user-defined meanings in memory (`unknown_inputs.json`) for future improvement.

### Track Progress
- Mood history and emotional trends are visualized and securely stored in `mood_tracker.db`.

---

## 💻 Installation

```bash
git clone https://github.com/barnazaka/calmbot.git
cd calmbot
pip install flask python-telegram-bot google-generativeai python-dotenv textblob
python -m textblob.download_corpora
````

### Set Up Environment

Create a `.env` file in the `calmbot/` directory:

```
TELEGRAM_TOKEN=your_telegram_token
GOOGLE_API_KEY=your_gemini_api_key
```

* Place `index.html` in `calmbot/templates/`
* Place audio files in `calmbot/static/`

### Run the Website

```bash
python server.py
```

Access at `http://localhost:5000`

### Run the Telegram Bot

```bash
python calmbot.py
```

---

## 🚀 Usage

### Website

* Select a mood, explore the Serenity Garden, start journaling, or chat.
* Track your healing journey visually.

### Telegram Bot

* Use `/start` to begin.
* Select a mood or type `/chat` to talk freely.
* Responses are adaptive and emotionally aware.

### Example Interaction

```text
User: I'm feeling stressed.
CalmBot: Stress can feel so heavy, often tied to life’s chaos or past worries. Try a 4-4-8 breathing exercise: inhale for 4, hold for 4, exhale for 8. Want to share more? I’m here.

User: xyz
CalmBot: I don’t know what you mean by "xyz," but I’ll learn! Can you explain it? Let’s keep chatting.
```

---

## 💖 Why CalmBot?

* **Trauma-Aware Design:** Tackles childhood wounds and emotional pain with empathy.
* **Dual AI Approach:** Combines Gemini’s power with a custom learner for personalization.
* **Accessible Platforms:** Website and Telegram support available 24/7.
* **Holistic Healing:** Journaling, breathing, mindfulness, and conversation in one place.
* **Privacy-First:** Stores data locally with SQLite for user security and trust.

---

## 📈 Future Enhancements

* Mobile App (iOS/Android)
* Deeper Learning Personalization
* Multilingual Support
* Wearable Device Integration
* Community Sharing & Support

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit changes: `git commit -m "Add your feature"`.
4. Push: `git push origin feature/your-feature`.
5. Open a pull request.

Please review our **Code of Conduct** and use **GitHub Issues** for feedback or bugs.

---

## 👥 Team

Built with ❤️ by **Kohdee Team** for Hackathon organized by the Deepfunding Developer Outreach.
Passionate about mental health, AI, and empowering healing journeys.

* 📧 Contact: barnazaka@gmail.com and galadima892@gmail.com
* 🐙 GitHub: barnazaka
* ✈️ Telegram: @calm56bot

---

## 🙏 Acknowledgments

* **Google Gemini:** For powering empathetic responses.
* **Freesound.org:** For CC0 calming sounds.
* **Open Source Community:** Flask, p5.js, and more.
