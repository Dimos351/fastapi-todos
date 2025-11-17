FastAPI CRUD + Simple Key Auth

A simple learning project built with **FastAPI**, featuring:

- Basic HTTP & REST concepts
- CRUD operations for Todo items (in-memory)
- Pydantic reques/response models
- Simple API Key authorization
- Fully testable through Postman, curl, or the built-in `/docs` Swagger UI

---

## 🚀 Features

### ✔ CRUD Endpoints
- `Get /todos` - list all todos
- `Post /todos` - create a new todos
- `Get /todos/{todo_id}` - get todo by ID
- `Put /todos/{todo_id}` - update an existing todo
- `Delete /todos/{todo_id}` - delete a todo

### ✔ Secure Endpoint

Protected with a simple API key (`x-api-key` header):
    GET /secure

### ✔ API Key Example

Add the header:
    x-api-key: supersecret

---

## 📦 Project Structure

    project/
    │
    ├── app/
    │   ├── main.py        # FastAPI application with routes
    │   ├── auth.py        # API key authorization logic
    │   ├── schemas.py     # Pydantic models
    │
    ├── README.md          # Project documentation
    └── requirements.txt   # Project dependencies

---

## 📚 Requirements

Install dependencies:

``` bash 
pip install -r requirements.txt
```

Or install manually.

---

## ▶ Running the Server

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

Server will be available at:

    http://127.0.0.1:8000

Swagger UI docs:

    http://127.0.0.1:8000/docs

---

## 🧪 Testing the API

### ✔ Test in Postman

Add this header:

    x-api-key: supersecret

Send request to:

    GET http://127.0.0.1:8000/secure

### ✔ Test with curl

``` bash
curl -H "x-api-key: supersecret" http://127.0.0.1:8000/secure
```

---

## 💾 Notes

-   Todos are stored **in memory** --- restarting the server resets
    them.
-   This project is for educational purposes.

---

## 📝 License

MIT License