CalmBot - AI-Powered Mental Health Companion

Table of Contents

Introduction
Features
Demo
Installation
Usage
Project Structure
Technologies Used
Contributing
License
Acknowledgements
Contact

Introduction
CalmBot is an innovative AI-powered mental health companion designed to provide empathetic, 24/7 support for users navigating their emotional well-being. Built for Hackathon 2025, CalmBot offers a web-based interface with a soothing, user-friendly design, enabling users to express their emotions through interactive buttons (Happy, Sad, Angry, Anxious) or engage in freeform conversation. With a unique learning feature that adapts to unknown inputs, CalmBot ensures accessibility, anonymity, and continuous improvement, addressing mental health stigma with compassion.
The project leverages a Flask backend, a responsive Tailwind CSS frontend, and a SQLite database to deliver long, motivational responses tailored to users' emotional states. Whether you're seeking encouragement during joyful moments or guidance through challenges, CalmBot is your trusted companion.
Features

Interactive Emotion Buttons: Select from Happy, Sad, Angry, or Anxious to receive detailed, five-paragraph responses filled with encouragement, practical coping strategies, and motivation.
Conversational Chat Interface: Engage in freeform dialogue with responses drawn from a 1,000-entry dataset, with a smooth, animated chat box that appears on demand.
Adaptive Learning Feature: Logs unknown user inputs to unknown_inputs.json and confirms learning with follow-up responses, enhancing the bot’s capabilities over time.
Beautiful, Empathetic UI: Features soothing gradients, Poppins typography, and smooth animations (e.g., button hover effects, slide-in chat) for a calming experience.
Data Privacy: Stores interactions in a SQLite database (mood_tracker.db) with HIPAA-compliant logging, ensuring user anonymity.
Responsive Design: Optimized for desktop and mobile, with a seamless flow from emotion selection to chat.

Demo
Watch our 3-minute demo video showcasing CalmBot’s features:
CalmBot Demo Video (Replace with your video link)
Screenshots:



Emotion Buttons
Chat Interface







(Add screenshots to a screenshots folder in your repo)
Installation
Follow these steps to set up CalmBot locally:
Prerequisites

Python 3.10+
pip
Git

Steps

Clone the Repository:
git clone https://github.com/yourusername/calmbot.git
cd calmbot


Install Dependencies:
pip install flask


Verify Dataset:Ensure model_log.json exists in the project root with 1,000 response pairs. If missing, regenerate:
python generate_log.py


Set Up Project Structure:Confirm the following files/folders:

server.py
templates/index.html
model_log.json
unknown_inputs.json
mood_tracker.db
generate_log.py



Troubleshooting

Missing model_log.json:Run python generate_log.py to create it.
Flask Errors:Verify Flask installation:python -c "import flask; print(flask.__version__)"



Usage

Run the Server:
python server.py


Access the Website:Open http://localhost:5000 in a web browser.

Interact with CalmBot:

Click an emotion button (Happy, Sad, Angry, Anxious) to view a tailored response.
Select "Continue the Conversation" to open the chat interface.
Type messages to engage with the bot, testing the learning feature with inputs like “Alot” followed by “Lots on my mind”.
Use the “How Are You Feeling Today?” button to return to emotion selection.


Check Logs:

View interaction logs:sqlite3 mood_tracker.db "SELECT * FROM responses LIMIT 5;"


Inspect unknown inputs:cat unknown_inputs.json





Project Structure
calmbot/
├── server.py              # Flask backend
├── templates/
│   └── index.html         # Frontend with Tailwind CSS
├── model_log.json         # 1,000 response pairs
├── unknown_inputs.json    # Logs unknown inputs
├── mood_tracker.db        # SQLite database
├── generate_log.py        # Script to generate model_log.json
├── README.md              # Project documentation
└── screenshots/           # Demo images

Technologies Used

Frontend:
HTML5
Tailwind CSS (CDN)
JavaScript (ES6)
Poppins Font (Google Fonts)


Backend:
Flask (Python)
SQLite


Data:
JSON (model_log.json, unknown_inputs.json)


Environment:
Python 3.10
Windows PowerShell



Contributing
We welcome contributions to enhance CalmBot! To contribute:

Fork the Repository:Click "Fork" on GitHub.

Create a Branch:
git checkout -b feature/your-feature


Make Changes:Update code, ensuring compatibility with Flask and Tailwind CSS.

Test Locally:Run python server.py and verify at http://localhost:5000.

Submit a Pull Request:Push changes and open a PR with a clear description.


Guidelines:

Follow PEP 8 for Python code.
Maintain the empathetic tone in UI text.
Test all features (buttons, chat, learning).

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements

Hackathon 2025: For inspiring this project.
xAI: For providing Grok 3, which guided development.
Mental Health Community: For emphasizing the need for accessible support tools.
Tailwind CSS & Poppins: For enabling a beautiful UI.

Contact
For questions or collaboration:

Email: your.email@example.com
GitHub: yourusername
Support: support@calmbot.com

Built with empathy for Hackathon 2025 by [Your Name].
