# 🤖 Agentic Study AI

An intelligent **Agentic AI-powered study assistant** that helps users learn efficiently by generating study plans, explanations, quizzes, and enabling PDF-based question answering.

Built using **Flask, Groq LLMs, and PDF processing**, this project transforms static learning resources into an interactive AI-driven study system.

---

## 🚀 Features

### 🧠 Agentic AI System

* Automatically decides what actions are required based on user input
* Supports:

  * 📅 Study Plan Generation
  * 📘 Concept Explanation
  * 📝 Quiz Creation

---

### 💬 Smart Chat System

* Multi-chat support with separate memory
* Chat history maintained using session
* Clean ChatGPT-like UI

---

### 📄 PDF Analysis

* Upload single or multiple PDFs
* Extract and analyze document content
* Generate:

  * 📘 Summary
  * 📌 Key Points
  * 📝 Quiz Questions

---

### 🔍 Ask Questions from PDF

* Ask questions in natural language
* AI answers using **only uploaded PDF content**
* Context-aware responses

---

### 📂 Multi-Chat Memory

* Each chat maintains:

  * Independent history
  * Separate context
* Easily switch between chats

---

## 🏗️ Tech Stack

| Component      | Technology           |
| -------------- | -------------------- |
| Frontend       | HTML, CSS            |
| Backend        | Flask (Python)       |
| LLM API        | Groq (LLaMA 3.3 70B) |
| PDF Processing | PyPDF2               |
| State Mgmt     | Flask Session        |

---

## ⚙️ How It Works

1. User enters a query or uploads PDF
2. System identifies input type:

   * Text → Agent decision system
   * PDF → Text extraction
3. Agent decides required actions
4. Executes tools (planner, tutor, quiz)
5. AI generates structured response
6. Output is displayed in chat interface
7. Data stored in session for context

---

## 📸 Demo Flow

### 💬 Chat Mode

1. Enter a topic
2. Get:

   * Study plan
   * Explanation
   * Quiz

---

### 📄 PDF Mode

1. Upload PDF
2. AI generates:

   * Summary
   * Key points
   * Quiz

---

### 🔍 PDF Question Answering

1. Upload PDF
2. Ask question
3. Get answer based on document content

---

## ▶️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/agentic-study-ai.git
cd agentic-study-ai
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Set API Key (IMPORTANT)

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```

⚠️ **Do NOT share your API key publicly.**

---

## ▶️ Run App

```bash
python run.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```bash
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
```

---

## 🧪 Use Cases

* 📚 Study planning and revision
* 📄 Understanding PDFs and notes
* 🧾 Quick concept explanations
* 🏫 Academic learning
* 📝 Self-assessment using quizzes

---

## ⚠️ Limitations

* Uses session-based memory (not persistent)
* Large PDFs may slow response
* No vector database (basic retrieval approach)

---

## 🔮 Future Improvements

* 💾 Database for persistent chat history
* 🔍 Vector search (RAG for PDFs)
* 🎤 Voice input
* ⚡ Streaming responses
* 🌐 Cloud deployment

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## ⭐ Support

If you found this project useful:

* ⭐ Star this repository
* 📢 Share it with others

---

## 👨‍💻 Author

**Abhinav Anand**

---

## 📬 Contact

For queries or collaboration, feel free to reach out!
