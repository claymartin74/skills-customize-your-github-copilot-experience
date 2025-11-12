# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will learn how to design and implement a simple REST API using the FastAPI framework. The assignment covers defining endpoints, request/response models, basic validation, and running the application locally.

## 📝 Tasks

### 🛠️	Create a Todo REST API

#### Description
Build a small RESTful API for managing a todo list. Implement endpoints to create, read, update, and delete todo items. Use Pydantic models for request validation and in-memory storage for simplicity.

#### Requirements
Completed program should:

- Run a FastAPI application and serve endpoints on `http://localhost:8000`.
- Provide endpoints: `GET /todos`, `GET /todos/{id}`, `POST /todos`, `PUT /todos/{id}`, `DELETE /todos/{id}`.
- Use Pydantic models for request and response shapes.
- Validate input (e.g., `title` is required and `completed` is boolean).
- Include simple in-memory storage (list or dict) — no database required.
- Provide OpenAPI docs available at `/docs`.

### 🛠️	Add Tests (Optional)

#### Description
Write a few pytest tests to verify API behavior using the `TestClient` from `fastapi.testclient`.

#### Requirements
Completed tests should:

- Verify creating a todo returns `201` and the created item.
- Verify retrieving all todos returns a list.
- Verify updating and deleting behave as expected.


---

### Starter Files

- `starter-app.py` — A minimal FastAPI application scaffold to get started.
- `requirements.txt` — Python dependencies for the assignment.

---

If you want, you can extend this assignment by adding persistent storage (SQLite), authentication, or filtering and pagination for the `GET /todos` endpoint.
