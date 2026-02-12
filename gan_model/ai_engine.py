import os
import requests
import json

def generate_academic_response(prompt: str) -> str:
    try:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            return "API key not configured."

        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={api_key}"

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        result = response.json()

        return result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        return f"AI ERROR: {str(e)}"
