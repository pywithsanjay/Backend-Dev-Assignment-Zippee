# Backend-Dev-Assignment-Zippee


Love this — let’s make your GitHub page look **professional, clean, and recruiter-impressive** 💼🔥
Below is a **beautiful, production-style README** you can copy directly into `README.md`.

---

# 🚀 Task Manager API — Flask Enterprise Backend

> A modular, session-authenticated REST API built with Flask using clean architecture, environment-based configuration, and persistent storage. Designed to simulate real-world backend systems with protected routes, pagination, validation, and enterprise-grade structure.

---

## ✨ Features

### 🔐 Authentication & Security

* User Registration & Login
* Password Hashing (SHA-256)
* Session-Based Authentication (24-hour expiry)
* Protected Routes with Middleware
* Automatic Session Cleanup

### 📝 Task Management

* Create Task
* Get All Tasks (Paginated — 10 per page)
* Get Task by ID
* Update Task (Title & Description Required)
* Delete Task
* Auto Timestamp Management

### 🏗 Architecture

* Flask App Factory Pattern
* Blueprints for Modular Routing
* Clean Package Structure
* Environment-Based Configuration
* Centralized Logging System

### 💾 Storage

* JSON-Based Persistent Storage
* Separated Domains:

  * Users
  * Sessions
  * Tasks

---

## 📂 Project Structure

```
Task_manager/
│
├── logs/
│   └── app.log
│
├── app/
│   ├── __init__.py        # App factory
│   ├── config.py        # Environment configuration
│   ├── extensions.py   # Logging setup
│
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py     # Register / Login
│   │   └── tasks.py   # Task CRUD
│
│   ├── users/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.json
│   │   └── sessions.json
│
│   └── storage/
│       └── data.json
│
├── .env
├── requirements.txt
└── run.py
```

---

## ⚙️ Tech Stack

* **Backend:** Python, Flask
* **Auth:** Session-Based Authentication
* **Storage:** JSON Files
* **Config:** Environment Variables
* **Logging:** File-based Logging

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

#### Activate

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Environment Setup

Create a `.env` file in root:

```env
FLASK_ENV=development
SECRET_KEY=supersecretkey
SESSION_HOURS=24
LOG_LEVEL=INFO
```

---

### 5️⃣ Run Server

```bash
python run.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 🔐 Authentication Flow

### Register

```
POST /api/register
```

```json
{
  "username": "admin",
  "password": "1234"
}
```

---

### Login

```
POST /api/login
```

Response:

```json
{
  "session_key": "abc123-session-key"
}
```

---

### Use Session Key in Headers

All protected routes require:

```
Session-Key: abc123-session-key
```

---

## 📡 API Endpoints

### 👤 Auth

| Method | Endpoint      | Description               |
| ------ | ------------- | ------------------------- |
| POST   | /api/register | Register new user         |
| POST   | /api/login    | Login and get session key |

---

### 📝 Tasks

| Method | Endpoint               | Description           |
| ------ | ---------------------- | --------------------- |
| GET    | /api/tasks?page=1      | Get tasks (Paginated) |
| GET    | /api/tasks/<id>        | Get task by ID        |
| POST   | /api/add/task          | Create new task       |
| PUT    | /api/task/update/<id>  | Update task           |
| DELETE | /api/remove/tasks/<id> | Delete task           |

---

## 🧪 Postman Testing Guide

### Login First

Save session key automatically in Postman:

```javascript
pm.environment.set("SESSION_KEY", pm.response.json().session_key);
```

### Use in Headers

```
Session-Key: {{SESSION_KEY}}
```

---

## 📦 Example Create Task Request

```
POST /api/add/task
```

```json
{
  "title": "Build API",
  "description": "Implement session-based authentication"
}
```

---

## 📜 Logging

Logs are written to:

```
logs/app.log
```

Includes:

* Server startup
* Requests
* Errors
* Authentication activity

---

## 🛡 Validation Rules

* Title and Description required for updates
* Completed must be boolean
* Invalid sessions blocked
* Expired sessions auto-deleted

---

## 🧠 Design Highlights

* Clean separation of concerns
* Portable file paths
* Modular imports
* Scalable architecture
* Production-style error handling

---

## 🚀 Future Enhancements

* SQLite / PostgreSQL Database
* JWT Authentication
* Role-Based Access (Admin/User)
* Swagger API Docs
* Docker Deployment
* CI/CD (GitHub Actions)

---

## 🏆 Resume-Ready Description

> Built a modular Flask-based REST API using session-based authentication, protected routes, pagination, and environment-based configuration. Designed with enterprise architecture principles including clean package structure, logging, and persistent storage.

---

## 👨‍💻 Author

**Your Name**
Backend Developer — Python | Flask | REST APIs

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub — it helps a lot!

---

# 🎯 Want a Power Upgrade?

I can generate for you:
✅ **Swagger UI (`/docs`)**
✅ **Dockerfile + Deployment Guide**
✅ **GitHub Actions CI**
✅ **Database Version (SQLite/Postgres)**

Just say **“Make it production deployable”** 🚀
