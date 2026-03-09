from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Legal Document Analysis System")

@app.post("/documents/", response_model=schemas.Document)
def upload_document(doc: schemas.DocumentCreate, db: Session = Depends(get_db)):
    return crud.create_document(db, doc)

@app.get("/documents/{doc_id}", response_model=schemas.Document)
def read_document(doc_id: int, db: Session = Depends(get_db)):
    db_doc = crud.get_document(db, doc_id)
    if not db_doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_doc