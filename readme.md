# 📄 AI Notes Summarizer

An AI-powered web application that summarizes PDF notes into concise, exam-friendly study material using Large Language Models (LLMs). Users can upload a PDF, generate a structured summary, and download the summarized notes as a PDF.

---

## 🚀 Features

- 📤 Upload PDF notes
- 📖 Extract text from PDF automatically
- 🤖 AI-powered summarization using Groq LLM
- 📝 Exam-friendly structured summaries
- 📥 Download summarized notes as PDF
- ⚡ FastAPI backend
- 🎨 Clean and responsive frontend

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- FastAPI
- Python

### AI Model
- Groq API
- OpenAI Compatible SDK
- GPT OSS / Llama Models

### PDF Processing
- PyPDF2
- ReportLab

---

## 📂 Project Structure

```
Notes_summarizer/
│
├── backend/
│   ├── main.py
│   ├── pdf_reader.py
│   ├── summarizer.py
│   ├── pdf_generator.py
│   ├── uploads/
│   └── generated/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Notes-Summarizer.git

cd AI-Notes-Summarizer
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

For Groq

```env
GROQ_API_KEY=your_api_key_here
```

If using OpenAI

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Backend

```bash
python -m uvicorn backend.main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

## 🌐 Running the Frontend

Navigate to the frontend folder

```bash
cd frontend
```

Run a local server

```bash
python -m http.server 5500
```

Open

```
http://localhost:5500
```

---

## 📌 How It Works

1. Upload a PDF.
2. Backend extracts the text.
3. AI summarizes the content.
4. Summary is converted into a PDF.
5. User can read the summary or download the generated PDF.

## 🎯 Use Cases

- Students
- Teachers
- Competitive Exam Preparation
- Researchers
- Professionals

---
## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Parth Sharma and team**

B.Tech Artificial Intelligence & Machine Learning
