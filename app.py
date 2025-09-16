from flask import Flask, request
from gradio_client import Client

app = Flask(__name__)

# HuggingFace Space details
HF_API_KEY = "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"
HF_SPACE_URL = "https://dopami9-devta.hf.space"
API_NAME = "/chat"   # we’ll confirm this using test_hf_client.py

client = Client(HF_SPACE_URL, hf_token=HF_API_KEY)

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.form.get("Body", "")
    try:
        # Send user query to HuggingFace Space
        resp = client.predict(user_msg, api_name="/chat")
        bot_reply = resp[0] if isinstance(resp, (list, tuple)) else str(resp)
    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    return f"<Response><Message>{bot_reply}</Message></Response>", 200, {"Content-Type": "application/xml"}

if __name__ == "__main__":
    app.run(port=5000)