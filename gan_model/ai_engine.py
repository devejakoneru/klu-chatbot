import os
from google import genai

def generate_academic_response(prompt: str) -> str:
    try:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            return "API key not configured."

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"AI ERROR: {str(e)}"
