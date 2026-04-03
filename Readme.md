# 🎓 Agentic Study AI

Agentic Study AI is an AI-powered learning assistant that helps students understand content smarter by supporting both **PDF-based learning** and **interactive chat**.

---

## 🚀 Features

- 📄 Upload PDF documents  
- 💬 Ask questions directly (chat mode)  
- 🧠 AI-powered answers and explanations  
- 🔍 Context-based responses from PDFs  
- ⚡ Fast and interactive responses  
- 🔐 Secure API key handling using `.env`  

---

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
│   ├── css/
│   │   └── style.css      # Styling
│
├── .env                   # API keys
├── requirements.txt
├── run.py

## 🛠 Tech Stack

- Python  
- Flask (or backend script)  
- Groq API  
- PyPDF2  
- dotenv  

---

## 📦 How to Run

1️⃣ Clone Repository
git clone https://github.com/your-username/agentic-study-ai.git
cd agentic-study-ai
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run App
python run.py
