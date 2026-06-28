# pdf_summarizer# 📄 AI PDF Summarizer

An AI-powered PDF summarizer built with Python. The application extracts text from PDF documents, cleans the extracted content, and generates concise summaries using an LLM (Groq API).

## 🚀 Features

- 📄 Extract text from PDF files
- 🧹 Clean and preprocess extracted text
- 🤖 Generate AI-powered summaries
- 🔐 Secure API key management using `.env`
- 📝 Save extracted text for debugging
- 🏗️ Modular Python project structure

---

## 📂 Project Structure

```
pdf_summarizer/
│
├── app.py                 # Main application
├── pdf_reader.py          # PDF text extraction
├── summarizer.py          # AI summarization
├── utils.py               # Helper functions
├── sample.pdf             # Sample PDF
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3
- PyPDF
- Groq API
- OpenAI Python SDK
- python-dotenv

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AdenSial/pdf_summarizer.git
```

Navigate to the project:

```bash
cd pdf_summarizer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 📌 Example Workflow

```
PDF
   │
   ▼
Extract Text
   │
   ▼
Clean Text
   │
   ▼
Send to Groq LLM
   │
   ▼
Generate Summary
```

---

## 📷 Sample Output

```
========== SUMMARY ==========

This document discusses...
```

---

## 📚 What I Learned

- Working with PDF files using PyPDF
- Text preprocessing in Python
- Prompt engineering
- Using LLM APIs
- Managing API keys securely
- Building modular Python applications
- Git and GitHub workflow

---

## 👨‍💻 Author

**Aden Sial**

GitHub: https://github.com/AdenSial