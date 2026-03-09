from pydantic import BaseModel

class DocumentBase(BaseModel):
    title: str

class DocumentCreate(DocumentBase):
    content: str

class Document(DocumentBase):
    id: int
    extracted_data: str

    class Config:
        orm_mode = True