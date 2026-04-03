from services.gemini_service import generate_text

def quiz_agent(topic):
    return generate_text(f"Generate 3 quiz questions with answers on {topic}")