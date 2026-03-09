from sqlalchemy.orm import Session
import models, schemas
from utils import extract_entities

def create_document(db: Session, doc: schemas.DocumentCreate):
    extracted = extract_entities(doc.content)
    db_doc = models.Document(title=doc.title, content=doc.content, extracted_data=extracted)
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc

def get_document(db: Session, doc_id: int):
    return db.query(models.Document).filter(models.Document.id == doc_id).first()