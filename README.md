# Legal Document Analysis System 
 
![Python](https://img.shields.io/badge/Python-3.11-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-green) 
 
## Overview 
This project is a **FastAPI backend** for uploading and extracting structured information from legal documents. It supports **PDF, DOCX, and TXT** files and uses **spaCy** for NLP entity extraction. 
 
## Features 
- Upload legal documents via REST API 
- Extract structured data (case numbers, parties, dates, keywords) 
- Store extracted data in a database (SQLite by default) 
- Query documents using API endpoints 
 
## Tech Stack 
- Python 3.x 
- FastAPI 
- SQLAlchemy (SQLite / PostgreSQL) 
- spaCy (NLP) 
- Uvicorn (ASGI server) 
 
## Setup Instructions 
```bash 
git clone https://github.com/andreyessel/ai-legal-document-assistant2.0.git 
cd legal_document_analysis 
python -m venv venv 
venv\Scripts\activate 
pip install -r requirements.txt 
uvicorn main:app --reload 
``` 
 
## API Endpoints 
- **POST** `/documents/` - Upload a document (JSON: `{"title": "...", "content": "..."}`) 
- **GET** `/documents/{id}` - Retrieve a document with structured data 
 
## Example Request 
```bash 
curl -X POST "http://127.0.0.1:8000/documents/" -H "Content-Type: application/json" -d "{\"title\": \"Case A\", \"content\": \"This is the document content.\"}" 
``` 
 
## License 
MIT License 
