# Legal Document Analysis System 
 
## Overview 
A FastAPI backend to upload and extract structured data from legal documents. Supports PDF, DOCX, TXT. 
 
## Tech Stack 
- Python 
- FastAPI 
- SQLAlchemy (SQLite) 
- spaCy for NLP 
 
## Setup 
git clone https://github.com/andreyessel/ai-legal-document-assistant2.0.git 
cd legal_document_analysis 
python -m venv venv 
venv\Scripts\activate 
pip install -r requirements.txt 
uvicorn main:app --reload 
 
## API Endpoints 
- POST /documents/ - Upload a document 
- GET /documents/{id} - Retrieve a document 
