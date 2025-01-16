import requests
import json

BASE_URL = "http://localhost:8000"

def test_endpoints():
    # Test /test endpoint
    test_response = requests.get(f"{BASE_URL}/test")
    print("Test Endpoint:", test_response.json())

    # Test /chat endpoint
    chat_data = {"message": "Tell me about PM Kisan Scheme"}
    chat_response = requests.post(
        f"{BASE_URL}/chat",
        json=chat_data,
        headers={"Content-Type": "application/json"}
    )
    print("\nChat Response:", chat_response.json())

if __name__ == "__main__":
    test_endpoints()