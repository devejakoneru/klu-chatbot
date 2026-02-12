import os
import google.generativeai as genai

# Get API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")


def generate_academic_response(user_query: str) -> str:
    """
    Generates response only for university / academic related queries.
    """

    system_prompt = """
    You are KLU Campus Assistant.
    Only answer questions related to:
    - KL University
    - Academics
    - ERP
    - Exams
    - Placements
    - Study advice
    - CGPA improvement
    - Courses and syllabus

    If the question is unrelated, respond strictly:
    "I can only assist with KLU and study-related queries."
    """

    try:
        response = model.generate_content(system_prompt + "\nUser: " + user_query)
        return response.text
    except Exception:
        return "AI service is currently unavailable. Please try again later."
