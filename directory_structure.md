├── task_manager/
│   ├── requirements.txt
│   ├── alembic.ini
│   ├── README.md
│   ├── .env
│   ├── app/
│   │   ├── db.py
│   │   ├── config.py
│   │   ├── models.py
│   │   ├── background.py
│   │   ├── middlewares.py
│   │   ├── utils.py
│   │   ├── main.py
│   │   └── dependencies.py
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   ├── tasks.py
│   │   │   ├── users.py
│   │   │   └── websocket.py
│   │   ├── auth/
│   │   │   ├── oauth2.py
│   │   │   └── jwt.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── task.py
│   │   │   └── base.py
│   │   ├── schemas/
│   │   │   ├── user.py
│   │   │   └── task.py
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_auth.py
│   │   ├── test_websocket.py
│   │   └── test_tasks.py
│   ├── alembic/
│   │   ├── script.py.mako
│   │   ├── env.py
│   │   └── README
│   │   └── versions/
