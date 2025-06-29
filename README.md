# 📚 FastAPI Book Library API

A simple RESTful API to manage a book library using FastAPI.  
It allows users to add, list, retrieve, and delete books. Each book has a UUID and validated fields.

---

## 🚀 Features

- Add a book
- List all books
- Get a book by ID
- Delete a book by ID
- Validates that `year` is between 1 and 2100

---

## ▶️ How to Run

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

Docs:  
- Swagger UI → http://127.0.0.1:8000/docs  
- ReDoc → http://127.0.0.1:8000/redoc  

---

## 🧪 Example Payload

```json
{
  "title": "1984",
  "author": "George Orwell",
  "year": 1949,
  "genre": "Dystopian"
}
```

---

## 📝 Notes

- Uses in-memory list (no database)
- Built for internship task demonstration
