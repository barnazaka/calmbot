# CalmBot - AI-Powered Mental Health Companion

## Introduction

CalmBot is an innovative AI-powered mental health companion designed to provide empathetic, 24/7 support for users navigating their emotional well-being. It offers two main ways for users to connect:

- **Website:** CalmBot has a dedicated web-based interface featuring a soothing, user-friendly design. Through the website, users can express emotions by clicking interactive mood buttons (Happy, Sad, Angry, Anxious) or engage in freeform conversation. The website experience is ideal for users who prefer a focused and distraction-free environment for mental health support.

- **Bot:** Recognizing that most people spend more time on social media and messaging platforms than visiting websites, CalmBot is also available as a conversational bot. This bot runs on platforms like Telegram (currently live as [@calm56bot](https://t.me/calm56bot)) and can be extended to WhatsApp, Instagram, Facebook Messenger, Twitter, Discord, and more. The bot format allows easy access for users seeking quick, anonymous emotional support right where they already communicate daily.

### Why both a website and a bot?

- **Website:** Provides a rich, immersive interface tailored to mental wellness, with calming visuals, smooth animations, and detailed responses to help users deeply reflect on their feelings.
  
- **Bot:** Offers instant, convenient access on popular social platforms where users already spend time, lowering the barrier to seeking help and increasing reach and engagement.

CalmBot’s AI model is flexible and powers both the website and the bot, delivering heartfelt, empathetic responses. It adapts continuously through a unique learning feature that handles unknown inputs, ensuring personalized, evolving support while maintaining user privacy and anonymity.

Under the hood, CalmBot is built with a Flask backend, a responsive Tailwind CSS frontend for the website, and a SQLite database to log interactions securely.

---

## Benefits

- **Interactive Mood Buttons:** Choose from Happy, Sad, Angry, or Anxious to receive detailed, five-paragraph responses filled with encouragement and coping strategies.  
- **Conversational Chat:** Engage in dynamic dialogue with responses from a 1,000-entry dataset, featuring an animated chat box that appears seamlessly.  
- **Adaptive Learning:** Logs unknown inputs to `unknown_inputs.json` and confirms learning, enhancing personalization.  
- **Elegant UI:** Features calming gradients, Poppins typography, and smooth animations for a serene experience.  
- **Privacy-First:** Stores interactions in `mood_tracker.db` with HIPAA-compliant logging, ensuring user anonymity.  
- **Responsive Design:** Optimized for desktop and mobile, with intuitive navigation from mood selection to chat.

---

## Demo

Explore CalmBot in our 3-minute demo video:  
*CalmBot Demo Video (Replace with your video link)*  

### Screenshots:

#### Mood Selection  
*(Add screenshots to a `screenshots` folder in your repo)*  

#### Chat Interface  

---

## Installation

### Prerequisites

- Python 3.10+  
- pip  
- Git

### Steps

```bash
# Clone the Repository
git clone https://github.com/yourusername/calmbot.git
cd calmbot

# Install Dependencies
pip install flask

# Verify Dataset
# Ensure model_log.json exists with 1,000 response pairs. If missing, regenerate:
python generate_log.py
````

---

## Set Up Structure

Confirm these files and folders exist:

* `server.py`
* `templates/index.html`
* `model_log.json`
* `unknown_inputs.json`
* `mood_tracker.db`
* `generate_log.py`

---

## Troubleshooting

* **Missing `model_log.json`:** Run

  ```bash
  python generate_log.py
  ```

* **Flask Errors: Check version**

  ```bash
  python -c "import flask; print(flask.__version__)"
  ```

---

## Usage

### Start the Server

```bash
python server.py
```

### Access CalmBot

Open [http://localhost:5000](http://localhost:5000) in your browser.

### Interact

* Click a mood button (Happy, Sad, Angry, Anxious) to view a response.
* Select **Continue the Conversation** to open the chat interface.
* Test the learning feature by typing “Alot”, then “Lots on my mind”.
* Use the **How Are You Feeling Today?** button to return to mood selection.

---

## Monitor Logs

```bash
# View interactions
sqlite3 mood_tracker.db "SELECT * FROM responses LIMIT 5;"

# Check unknown inputs
cat unknown_inputs.json
```

---

## Project Structure

```bash
calmbot/
├── server.py              # Flask backend
├── templates/
│   └── index.html         # Frontend UI
├── model_log.json         # Response dataset
├── unknown_inputs.json    # Unknown input logs
├── mood_tracker.db        # SQLite database
├── generate_log.py        # Dataset generator
├── README.md              # Documentation
└── screenshots/           # Demo images
```

---

## Technologies Used

**Frontend:**

* HTML5
* Tailwind CSS (CDN)
* JavaScript (ES6)
* Poppins Font (Google Fonts)

**Backend:**

* Flask (Python)
* SQLite

**Data:**

* JSON (`model_log.json`, `unknown_inputs.json`)

**Environment:**

* Python 3.10
* Windows PowerShell

---

## Contributing

We welcome contributions to make CalmBot even better!

* **Fork the Repository:** Click “Fork” on GitHub.
* **Create a Branch:**

  ```bash
  git checkout -b feature/your-feature
  ```
* **Make Changes:** Update code, ensuring compatibility.
* **Test Locally:** Run `python server.py` and test at [http://localhost:5000](http://localhost:5000).
* **Submit a Pull Request:** Push changes and open a PR with a detailed description.

### Guidelines

* Adhere to PEP 8 for Python.
* Preserve the empathetic tone in UI text.
* Test all features (moods, buttons, chat).

---

## License

MIT License
See LICENSE file for details.

---

## Acknowledgements

* Hackathon 2025, organized by DeepFunding Developer Outright Circle: For inspiring this project.
* Mental Health Community: For highlighting accessible support needs.
* Tailwind CSS & Poppins: For a beautiful UI.

---

## Contact

For inquiries or collaboration:

* **Email:** 
* **GitHub:** 
* **Support:** 
