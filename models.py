from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class Book(BaseModel):
    id: UUID
    title: str
    author: str
    year: int
    genre: Optional[str] = None


class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    genre: Optional[str] = None
