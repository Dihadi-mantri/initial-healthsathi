from gradio_client import Client

HF_API_KEY = "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"
BASE = "https://dopami9-devta.hf.space"

client = Client(BASE, hf_token=HF_API_KEY)

# Step 1: See available APIs
print("Available APIs:", client.view_api())

# Step 2: Test the chatbot
resp = client.predict("What are dengue symptoms?", api_name="/chat")
print("RAW RESPONSE:", resp)

if isinstance(resp, (list, tuple)) and len(resp) > 0:
    print("Bot Reply:", resp[0])
else:
    print("Bot Reply:", str(resp))
