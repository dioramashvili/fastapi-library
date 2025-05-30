from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID
from typing import List
from models import Book, BookCreate

app = FastAPI()

# In-memory "database"
books: List[Book] = []


@app.post("/books", response_model=Book)
def add_book(book_create: BookCreate):
    book = Book(id=uuid4(), **book_create.dict())
    books.append(book)
    return book


@app.get("/books", response_model=List[Book])
def list_books():
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: UUID):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: UUID):
    for index, book in enumerate(books):
        if book.id == book_id:
            return books.pop(index)
    raise HTTPException(status_code=404, detail="Book not found")
