from gradio_client import Client

# 1. Connect to the HealthSathi Space
# Note: based on your previous success, we don't need the hf_token if it's public.
print("🔌 Connecting to HealthSathi...")
client = Client("dopami9/Healthsathi")
print("✅ Connected!")

# 2. Define your test message
test_msg = "What are the symptoms of dengue?"
print(f"📤 Sending message: '{test_msg}'")

# 3. Send to the SPECIFIC endpoint shown in your screenshot
try:
    result = client.predict(
        user_message=test_msg,          # MUST match the screenshot parameter name
        api_name="/get_health_response" # MUST match the screenshot API name
    )
    
    print("\n--- 🤖 BOT RESPONSE ---")
    print(result)
    print("-----------------------")

except Exception as e:
    print(f"\n❌ Error: {e}")