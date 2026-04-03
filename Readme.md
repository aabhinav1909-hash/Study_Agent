🚀 📄 Agentic Study AI

An intelligent Agentic AI-powered study assistant that helps students learn smarter by generating study plans, explanations, quizzes, and analyzing PDFs.

Built using Flask, Groq LLMs, and PDF processing, this project transforms static study material into an interactive AI learning system.

🚀 Features
🧠 Agentic AI System
Automatically decides what to do based on user input
Supports:
📅 Study Plan Generation
📘 Concept Explanation
📝 Quiz Creation

💬 Smart Chat System
Multi-chat support
Chat history memory
ChatGPT-like UI
Separate context for each chat

📄 PDF Analysis
Upload single or multiple PDFs
Extract and analyze content
Generate:
📘 Summary
📌 Key Points
📝 Quiz Questions

🔍 Ask Questions from PDF
Ask queries in natural language
AI answers using only uploaded PDF content
Context-aware response

📌 Multi-Chat Memory
Each chat has:
Separate history
Independent context
Switch between chats easily

🏗️ Tech Stack
Component	Technology
Frontend	HTML, CSS
Backend	Flask (Python)
AI Model	Groq (LLaMA 3.3 70B)
PDF Processing	PyPDF2
State Mgmt	Flask Session

⚙️ How It Works
User enters query or uploads PDF
System processes input:
Text → Agent decides actions
PDF → Extract + analyze
AI generates structured response
Output displayed in chat interface

📂 Project Structure
study-agent/
│
├── app/
│   ├── routes.py          # Backend logic
│   ├── __init__.py        # Flask setup
│
├── services/
│   ├── groq_service.py    # AI API calls
│   ├── pdf_service.py     # PDF processing
│
├── templates/
│   ├── chat.html          # UI
│
├── static/
│   ├── css/style.css      # Styling
│
├── .env                   # API keys
├── requirements.txt
├── run.py

▶️ Installation & Setup

1️⃣ Clone Repository
git clone https://github.com/your-username/agentic-study-ai.git
cd agentic-study-ai

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt
🔑 Set API Key (IMPORTANT)
Create .env file:
GROQ_API_KEY=your_api_key_here
⚠️ Do NOT share your API key publicly.

▶️ Run App
python run.py
Open: http://127.0.0.1:5000

🧪 Use Cases

📚 Study planning and revision
📄 Understanding PDFs and notes
🧾 Quick concept explanations
🏫 Academic projects
📝 Self-testing via quizzes

⚠️ Limitations
Uses session-based memory (not permanent)
Large PDFs may slow response
No vector database (basic retrieval)

🔮 Future Improvements
💾 Database for persistent chats
🔍 Vector search (RAG for PDFs)
🎤 Voice input
⚡ Streaming responses
🌐 Cloud deployment

🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and improve.

⭐ Support

If you found this project useful:
⭐ Star this repository
📢 Share it with others

📬 Contact

For queries or collaboration, feel free to reach out.
