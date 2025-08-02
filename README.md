# RegexResumeParser - Smart Resume Parser & Validator

RegexResumeParser is an intelligent, end-to-end resume parser and validator built with **Python**, **Flask**, and **Regex**. It allows users to upload resumes in multiple formats (PDF, DOCX, TXT), extract structured data (name, email, phone, skills, education, etc.), and validate key fields.

## 🚀 Features

- 📤 Drag-and-drop file upload
- 📂 Bulk resume parsing
- 🧠 Regex-powered field extraction
- 🧪 Validation for email, phone, LinkedIn
- 📥 JSON export of parsed data
- 🗃️ Resume storage in SQLite database using SQLAlchemy
- 🔄 Loading spinner during parsing for better UX

## 📸 Demo

![demo gif](https://your-demo-url.com/demo.gif)

## 🛠️ Tech Stack

- Python 3.x
- Flask & Jinja2
- SQLAlchemy (SQLite)
- PyMuPDF (for PDF parsing)
- python-docx (for DOCX files)
- Regex (re module)
- HTML, CSS, JavaScript

## 📁 Project Structure

```
resume_parser/
├── app/
│ ├── parser/ # Regex logic and file parsing
│ ├── templates/ # Jinja2 templates
│ ├── static/ # CSS/JS files
│ ├── uploads/ # Temporarily uploaded resumes
│ ├── models.py # Resume DB model
│ ├── routes.py # Flask routes
│ └── init.py
├── run.py
├── requirements.txt
└── README.md
```

## 🧑‍💻 Installation

```bash
git clone https://github.com/yourusername/RegexResumeParser.git
cd RegexResumeParser
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python run.py
```

## Sample Output

```json
{
  "name": "Binayak Basu",
  "email": "binayak@example.com",
  "phone": "+91-9876543210",
  "linkedin": "https://linkedin.com/in/binayak",
  "education": ["B.Tech in Computer Science", "M.Tech in AI"],
  "skills": ["Python", "Flask", "Machine Learning"]
}
```

## 📦 Future Enhancements

- NLP-based name and skill extraction (spacy, transformers)
- Admin dashboard to view & download all resumes
- Resume ranking/matching with job descriptions
- Export to CSV/Excel
