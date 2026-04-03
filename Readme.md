🚀 📄 README.md
# 🤖 Agentic Study AI

An intelligent **Agentic AI-powered study assistant** that helps students learn, plan, and analyze study material efficiently.

---

## 🚀 Features

### 🧠 Agentic AI System
- Automatically decides what to do:
  - 📅 Generate study plans
  - 📘 Explain concepts
  - 📝 Create quizzes

### 💬 Smart Chat System
- Multi-chat support
- Chat history memory
- Clean ChatGPT-like UI

### 📄 PDF Analysis
- Upload single or multiple PDFs
- Extract and analyze content
- Generate:
  - Summary
  - Key points
  - Quiz questions

### 🔍 Ask Questions from PDF
- Ask queries based on uploaded documents
- Context-aware answers

---

## 🏗️ Tech Stack

| Layer       | Technology        |
|------------|------------------|
| Frontend   | HTML, CSS        |
| Backend    | Flask (Python)   |
| AI Model   | Groq API (LLM)   |
| PDF Parser | PyPDF2           |
| State Mgmt | Flask Session    |

---

## 🧠 How It Works

1. User enters query or uploads PDF
2. Agent decides required actions:
   - planner / tutor / quiz
3. System executes multiple AI calls
4. Response is displayed in structured format

---

## 📂 Project Structure


study-agent/
│
├── app/
│ ├── routes.py # Main backend logic
│ ├── init.py # Flask setup
│
├── services/
│ ├── groq_service.py # AI API calls
│ ├── pdf_service.py # PDF processing
│
├── templates/
│ ├── chat.html # Frontend UI
│
├── static/
│ ├── css/style.css # Styling
│
├── .env # API keys
├── requirements.txt
├── run.py # App entry point


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/agentic-study-ai.git
cd agentic-study-ai
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add API Key

Create .env file:

GROQ_API_KEY=your_api_key_here
5️⃣ Run App
python run.py

Open:

http://127.0.0.1:5000
🎬 Demo
💬 Chat Example
Input: Learn Python
Output:
- Study Plan
- Explanation
- Quiz
📄 PDF Example
Upload PDF
Get:
Summary
Key Points
Quiz
🧪 Future Improvements
💾 Database (persistent chat history)
🔍 Vector search (RAG for PDFs)
🎤 Voice input
⚡ Streaming responses
🌐 Deployment (cloud hosting)
🤝 Contributing

Contributions are welcome!
Feel free to fork and improve.

📜 License

This project is for educational purposes.

👨‍💻 Author

Abhinav Anand

⭐ If you like this project, give it a star!


---

# 🔥 BONUS (IMPORTANT)

👉 Replace:
```text
your-username

with your GitHub username
