# Limkokwing Library Management API

## Project Overview

The Limkokwing Library Management API is a RESTful backend system built using FastAPI and PostgreSQL.

The system enables administrators and librarians to manage library resources while allowing members to browse books and submit reviews.

The project demonstrates:

- FastAPI Development
- PostgreSQL Integration
- SQLAlchemy ORM
- JWT Authentication
- Role-Based Access Control
- Dependency Injection
- Async Programming
- REST API Design
- Open Source Development

---

## SDG Alignment

This project supports:

### SDG 4 – Quality Education

The system improves access to educational resources by organizing books, authors, reviews, and borrowing records within a centralized platform.

---

## Technologies Used

- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT
- Passlib
- Python-Jose
- Pydantic
- Uvicorn

---

## User Roles

### Admin

Can:

- Create Users
- Delete Users
- View Users
- Manage Books
- Manage Authors
- Manage Reviews

### Librarian

Can:

- Create Books
- Update Books
- Delete Books
- Manage Authors
- Borrow Books
- Return Books

### Member

Can:

- View Books
- View Authors
- Create Reviews
- View Reviews

---

## Authentication

JWT Authentication using:

- OAuth2PasswordBearer
- Access Tokens
- Password Hashing with bcrypt

---

## API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

---

## Installation

Create Virtual Environment

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Project

```bash
uvicorn app.main:app --reload
```

---

## Environment Variables

```env
DATABASE_URL=postgresql://postgres:password@localhost/library_management

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Open Source License

MIT License