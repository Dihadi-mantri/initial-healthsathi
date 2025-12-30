from flask import Flask, request
from gradio_client import Client
import os

app = Flask(__name__)

# Config
HF_SPACE_URL = "dopami9/Healthsathi"
API_NAME = "/get_health_response"

print(f"🔗 Connecting to Hugging Face Space: {HF_SPACE_URL}...")

client = None
try:
    client = Client(HF_SPACE_URL)
    print("✅ Connected to Brain successfully!")
except Exception as e:
    print(f"❌ Connection Failed: {e}")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.form.get("Body", "")
    sender = request.form.get("From", "")
    print(f"📩 Message from {sender}: {user_msg}")

    bot_reply = ""
    try:
        if not client:
            raise ConnectionError("Client is not connected.")
        resp = client.predict(
            user_message=user_msg, 
            api_name=API_NAME
        )
        
        bot_reply = str(resp)
        print(f"🤖 Bot Replied: {bot_reply}")
        
    except Exception as e:
        print(f"❌ Prediction Error: {e}")
        bot_reply = "HealthSathi is sleeping. Please wake him up later."

    return f"<Response><Message>{bot_reply}</Message></Response>", 200, {"Content-Type": "application/xml"}

if __name__ == "__main__":
    app.run(port=5000)