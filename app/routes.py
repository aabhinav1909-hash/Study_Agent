from flask import Blueprint, render_template, request, session, redirect, url_for
from services import generate_text
from services.pdf_service import analyze_pdf, ask_pdf_question

main = Blueprint("main", __name__)


# 🧠 Agent decision
def agent_decision(user_input):
    prompt = f"""
    Decide what is needed for this request:
    "{user_input}"

    Available:
    - planner
    - tutor
    - quiz

    Return ONLY comma separated values.
    """

    try:
        actions = generate_text(prompt).lower()
    except:
        actions = ""

    valid = ["planner", "tutor", "quiz"]
    selected = [a for a in valid if a in actions]

    return selected if selected else ["tutor"]


# ⚙️ Agent execution
def run_agent(user_input):
    actions = agent_decision(user_input)
    output = ""

    try:
        if "planner" in actions:
            output += "<div class='card'><h3>📅 Study Plan</h3>"
            output += generate_text(f"Create a simple study plan for {user_input}")
            output += "</div>"

        if "tutor" in actions:
            output += "<div class='card'><h3>📘 Explanation</h3>"
            output += generate_text(f"Explain {user_input} clearly")
            output += "</div>"

        if "quiz" in actions:
            output += "<div class='card'><h3>📝 Quiz</h3>"
            output += generate_text(f"Create 3 quiz questions on {user_input}")
            output += "</div>"

    except Exception as e:
        output = f"<p class='error'>⚠️ Error: {str(e)}</p>"

    if not output.strip():
        output = "<p class='error'>⚠️ No response generated.</p>"

    return output


@main.route("/", methods=["GET", "POST"])
def chat():

    # 🔹 Initialize session
    if "conversations" not in session:
        session["conversations"] = {}

    if "current_chat" not in session:
        session["current_chat"] = "chat1"
        session["conversations"]["chat1"] = {
            "messages": [],
            "title": "New Chat"
        }

    # 🔹 Initialize PDF storage (SAFE way)
    if "pdf_text" not in session:
        session["pdf_text"] = ""
    if "pdf_names" not in session:
        session["pdf_names"] = []

    if request.method == "POST":

        chat_id = session["current_chat"]

        # 🔥 MULTIPLE PDF UPLOAD
        pdf_files = request.files.getlist("pdf")

        if pdf_files and pdf_files[0].filename != "":

            from services.pdf_service import extract_text_from_multiple_pdfs

            text = extract_text_from_multiple_pdfs(pdf_files)

            # Save only TEXT (safe for session)
            session["pdf_text"] = text
            session["pdf_names"] = [f.filename for f in pdf_files]

            ai_response = generate_text(f"""
            Analyze this PDF content:

            {text}

            Give:
            1. Summary
            2. Key Points
            3. 5 Quiz Questions with answers
            """)

            session["conversations"][chat_id]["messages"].append({
                "role": "ai",
                "content": f"<div class='card'><h3>📄 PDF Analysis</h3>{ai_response}</div>"
            })

        else:
            user_input = request.form.get("topic", "").strip()

            if not user_input:
                return redirect(url_for("main.chat"))

            # 🧠 Set title
            if session["conversations"][chat_id]["title"] == "New Chat":
                session["conversations"][chat_id]["title"] = user_input[:20]

            # 👤 User message
            session["conversations"][chat_id]["messages"].append({
                "role": "user",
                "content": user_input
            })

            # 🔥 If PDF exists → answer from PDF
            if session.get("pdf_text"):
                ai_response = generate_text(f"""
                Answer using ONLY this PDF content:

                {session['pdf_text']}

                Question: {user_input}
                """)
            else:
                ai_response = run_agent(user_input)

            # 🤖 AI response
            session["conversations"][chat_id]["messages"].append({
                "role": "ai",
                "content": ai_response
            })

        session.modified = True

    return render_template(
        "chat.html",
        chats=session["conversations"],
        current_chat=session["current_chat"],
        pdf_names=session.get("pdf_names", [])
    )


# ➕ New chat
@main.route("/new_chat")
def new_chat():
    if "conversations" not in session:
        session["conversations"] = {}

    chat_id = f"chat{len(session['conversations']) + 1}"

    session["conversations"][chat_id] = {
        "messages": [],
        "title": "New Chat"
    }

    # 🔥 Reset PDF when new chat starts
    session["pdf_text"] = ""
    session["pdf_names"] = []

    session["current_chat"] = chat_id
    session.modified = True

    return redirect(url_for("main.chat"))


# 🔄 Switch chat
@main.route("/switch_chat/<chat_id>")
def switch_chat(chat_id):
    session["current_chat"] = chat_id
    session.modified = True
    return redirect(url_for("main.chat"))