# FastAPI Todo API — Clean Structure Learning Project

This project is a **learning-friendly FastAPI application** that demonstrates how to build a clean and maintainable API using:

- FastAPI routers  
- Pydantic models (schemas)  
- A simple in-memory data store  
- Clean separation of concerns (routes → CRUD → storage → schemas)  
- Basic API Key authentication  

Designed for beginners who want to understand **proper backend structure**, not just “make an endpoint work”.

---

# 🚀 Features

### ✔ CRUD Endpoints
All endpoints operate on an in-memory Todo list:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/todos` | List all todos |
| POST | `/todos` | Create a new todo |
| GET | `/todos/{todo_id}` | Get todo by ID |
| PUT | `/todos/{todo_id}` | Update an existing todo |
| DELETE | `/todos/{todo_id}` | Delete todo |

### ✔ Secure Endpoint
A simple API Key protected route:

```
GET /secure
```

Requires the header:

```
x-api-key: supersecret
```

### ✔ Clean Architecture (Educational)
The project is structured to imitate real-world backend design:

- **main.py** — HTTP layer (routes only)
- **crud.py** — business logic and data transformations
- **storage.py** — in-memory “database” abstraction
- **schemas.py** — Pydantic models & validation
- **auth.py** — simple API key authentication

---

# 📦 Project Structure

```
project/
│
├── auth.py        # API key validation dependency
├── crud.py        # CRUD logic and helpers
├── main.py        # FastAPI app with route handlers
├── schemas.py     # Pydantic models for requests/responses
├── storage.py     # In-memory data storage class
│
├── README.md
└── requirements.txt
```

This structure teaches how to **avoid mixing routing, logic, and data storage** — a common beginner mistake.

---

# 🧠 How It Works (Architecture Explained)

### 1. **Routes (main.py)**  
Handle incoming HTTP requests and return responses.  
They **do not contain logic** — only call CRUD functions.

### 2. **CRUD Layer (crud.py)**  
Contains all business logic:

- updating fields  
- validating data  
- raising errors  

This keeps the API clean and testable.

### 3. **Storage Layer (storage.py)**  
An in-memory “database” wrapped in a class:

- `add()`  
- `get()`  
- `all()`  
- `delete()`  

Later, this can easily be swapped with PostgreSQL or SQLAlchemy.

### 4. **Schemas (schemas.py)**  
Define how todo items look:

- `Todo`
- `TodoCreate`
- `TodoUpdate`
- `TodoBase`

This ensures consistent request/response structure.

### 5. **Auth (auth.py)**  
Simple API key check using the `x-api-key` header.

---

# 📚 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install fastapi uvicorn pydantic
```

---

# ▶ Running the Server

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Interactive API docs:

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Testing the API

### ✔ Postman Example

Add the header:

```
x-api-key: supersecret
```

Request:

```
GET http://127.0.0.1:8000/secure
```

### ✔ curl Example

```bash
curl -H "x-api-key: supersecret" http://127.0.0.1:8000/secure
```

---

# 💾 Notes

- Todos are stored **in memory** — restarting the server resets all data.
- This project is intended for **learning clean architecture in FastAPI**, not production use.
- The design makes it easy to switch to a real database (PostgreSQL, SQLAlchemy, etc.)

---

# 🔮 Future Improvements (Suggested)

- Replace in-memory storage with PostgreSQL  
- Add SQLAlchemy models + Alembic migrations  
- Implement JWT authentication  
- Add pagination  
- Add unit tests using `pytest` and `TestClient`  
- Introduce service/repository layers (full Clean Architecture)

---

# 📝 License

MIT License
