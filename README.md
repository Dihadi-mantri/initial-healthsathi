```markdown
# Healthsathi 🏥

**Healthsathi** is an AI-powered health assistant designed to bridge the gap between complex medical knowledge and rural users via WhatsApp. It utilizes a Flask backend to connect users with a fine-tuned LLM hosted on Hugging Face, specifically optimized for vernacular languages (e.g., Bhojpuri, Hindi).

## 🚀 Features
- **WhatsApp Integration:** Users communicate via a standard WhatsApp interface.
- **Vernacular Support:** Understands and replies in local dialects (e.g., *"Hamar matha dukhat ba"*).
- **Real-time Inference:** Connects to a Hugging Face Space for instant AI responses.
- **Scalable Backend:** Built on Flask, ready for deployment on cloud platforms.

## 🛠️ Tech Stack
- **Backend Framework:** Python (Flask)
- **AI Inference:** Gradio Client (Hugging Face Spaces)
- **Messaging Interface:** Twilio API (WhatsApp)
- **Model Hosting:** Hugging Face

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/Dihadi-mantri/initial-healthsathi.git](https://github.com/Dihadi-mantri/initial-healthsathi.git)
   cd initial-healthsathi

```

2. **Create a Virtual Environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

```


3. **Install Dependencies**
```bash
pip install -r requirements.txt

```


4. **Run the Server**
```bash
python app.py

```


The server will start on `http://127.0.0.1:5000`.

## 📡 API Endpoints

### `POST /chat`

Handles incoming messages from Twilio/WhatsApp.

* **Input:** Standard Twilio form data (`Body`, `From`).
* **Output:** TwiML (Twilio Markup Language) XML response containing the AI's advice.

## ⚠️ Disclaimer

Healthsathi is an AI assistant and **does not replace a professional doctor**. It provides general health information and triage advice. Always consult a qualified medical professional for serious conditions.

---

*Built with ❤️ for accessible healthcare.*

```

```