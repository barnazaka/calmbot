# CalmBot - AI-Powered Mental Health Companion

## Table of Contents
- [Introduction](#introduction)  
- [Benefits](#benefits)  
- [Demo](#demo)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Technologies Used](#technologies-used)  
- [Contributing](#contributing)  
- [License](#license)  
- [Acknowledgements](#acknowledgements)  
- [Contact](#contact)  

---

## Introduction
CalmBot is an innovative AI-powered mental health companion designed to provide empathetic, 24/7 support for users navigating their emotional well-being. Built for Hackathon 2025, CalmBot offers a web-based interface with a soothing, user-friendly design, enabling users to express emotions through interactive buttons (Happy, Sad, Angry, Anxious) or engage in freeform conversation.

With a unique learning feature that adapts to unknown inputs, CalmBot ensures accessibility, anonymity, and continuous improvement, addressing mental health stigma with compassion. The project leverages a Flask backend, a responsive Tailwind CSS frontend, and a SQLite database to deliver heartfelt responses tailored to users' emotional states.

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
[CalmBot Demo Video](#) *(Replace with your video link)*

### Screenshots:
#### Mood Selection  
*(Add screenshot here)*

#### Chat Interface  
*(Add screenshot here)*

*(Add screenshots to a `screenshots` folder in your repo)*

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
