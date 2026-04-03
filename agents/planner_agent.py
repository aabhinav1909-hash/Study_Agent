from services.gemini_service import generate_text

def planner_agent(topic):
    return generate_text(f"Create a study plan for {topic}")