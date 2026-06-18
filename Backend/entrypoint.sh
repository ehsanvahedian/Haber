#!/bin/bash
cd /app/Backend

# نصب وابستگی‌ها
uv sync

# بررسی وجود دایرکتوری alembic
if [ ! -d "alembic" ]; then
    echo "Initializing alembic..."
    uv run alembic init alembic
fi

# کپی فایل‌های نمونه اگر وجود دارند
if [ -f "alembic.example.ini" ]; then
    mv alembic.example.ini ./alembic.ini
fi

if [ -f "alembic.env.example.py" ]; then
    mv alembic.env.example.py ./alembic/env.py
fi

# ایجاد migration اگر فایل alembic.ini وجود دارد
if [ -f "alembic.ini" ]; then
    echo "Creating migration..."
    uv run alembic revision --autogenerate -m "Tables added" || echo "No changes detected"
    echo "Running migrations..."
    uv run alembic upgrade head
else
    echo "alembic.ini not found, skipping migrations"
fi

# اجرای برنامه
echo "Starting application..."
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload