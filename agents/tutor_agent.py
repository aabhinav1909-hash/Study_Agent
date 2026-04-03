from services.gemini_service import generate_text

def tutor_agent(topic):
    return generate_text(f"Teach {topic} in simple terms with examples")