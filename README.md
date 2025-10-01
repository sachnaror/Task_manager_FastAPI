# Task Manager FastAPI Experiments

A simple but powerful **FastAPI-based Task Manager** 📝 that lets you:

- Create ✅, Update ✏️, Delete ❌, and View 👀 tasks.
- Manage users 👨‍👩‍👧‍👦 with authentication 🔑.
- Auto-generated **Swagger UI** and **ReDoc** for documentation.
- Powered by **PostgreSQL** 🐘 with **SQLAlchemy ORM**.

---

## 🌟 Features

- ⚡ **FastAPI** — high-performance Python web framework.
- 🐘 **Postgres** — persistent storage for tasks & users.
- 🔐 **JWT Auth** — secure login & token handling.
- 📚 **Alembic** — smooth database migrations.
- 🛠️ **Background tasks** — e.g., send email notifications.
- 📊 **Middleware logging** — track every request.
- 🧪 **Test suite** with `pytest`.

---

## 📂 Project Structure

```
task_manager/
│── app/
│   ├── main.py              # App entrypoint
│   ├── db.py                # DB connection
│   ├── config.py            # Env settings
│   ├── models/              # SQLAlchemy models
│   ├── schemas/             # Pydantic schemas
│   ├── routers/             # API routes
│   ├── core/                # Middlewares, background jobs, utils
│   └── auth/                # Auth & JWT
│── alembic/                 # Migrations
│── requirements.txt
│── alembic.ini
│── README.md
│── .env
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/sachnaror/task_manager.git
cd task_manager
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Postgres

Make sure Postgres is running 🐘. Create DB:
```bash
createdb task_manager
```

### 5️⃣ Run migrations

```bash
alembic upgrade head
```

### 6️⃣ Start the server

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

- Swagger UI: 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: 👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛠 Example Usage

### ➕ Create a Task
**POST** `/tasks`
```json
{
  "title": "Finish FastAPI Project",
  "description": "Implement CRUD for Task Manager",
  "completed": false
}
```

### 📋 Get All Tasks
**GET** `/tasks`
```json
[
  {
    "id": 1,
    "title": "Finish FastAPI Project",
    "description": "Implement CRUD for Task Manager",
    "completed": false
  }
]
```

### ✏️ Update a Task

**PUT** `/tasks/{task_id}`

### ❌ Delete a Task
**DELETE** `/tasks/{task_id}`

---

## 🧪 Running Tests
```bash
pytest -v
```

---

## 🔮 Roadmap

- ✅ Basic CRUD for tasks & users.
- 🔐 JWT Authentication.
- 📧 Email notifications via background jobs.
- 📊 Task status dashboard.
- 🕸 WebSocket real-time updates.

---

## 📩 Contact

| Name              | Details                                                                 |
|-------------------|-------------------------------------------------------------------------|
| **👨‍💻 Developer**  | Sachin Arora                                                            |
| **📧 Email**      | [sachnaror@gmail.com](mailto:sachnaror@gmail.com)                       |
| **📍 Location**   | Noida, India                                                            |
| **📂 GitHub**     | [Github.com/sachnaror](https://github.com/sachnaror)                    |
| **🌐 YouTube**    | [My_Youtube](https://www.youtube.com/@sachnaror4841/videos)             |
| **🌐 Blog**       | [My_Blog](https://medium.com/@schnaror)                                 |
| **🌐 Website**    | [About_Me](https://about.me/sachin-arora)                               |
| **🌐 Twitter**    | [Twitter](https://twitter.com/sachinhep)                                |
| **📱 Phone**      | [+91 9560330483](tel:+919560330483)                                     |

---

✨ Built with ❤️ using **FastAPI + PostgreSQL + SQLAlchemy**
