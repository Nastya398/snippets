from datetime import datetime

from pydantic import BaseModel


class SnippetCreate(BaseModel):
    title: str
    content: str

class SnippetResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
