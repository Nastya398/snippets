from pydantic import BaseModel
from datetime import datetime

class SnippetCreate(BaseModel):
    title: str
    content: str

class SnippetResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
