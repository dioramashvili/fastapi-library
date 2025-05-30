from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class BookCreate(BaseModel):
    title: str
    author: str
    year: int = Field(..., gt=0, lt=2100)
    genre: Optional[str] = None


class Book(BookCreate):
    id: UUID
