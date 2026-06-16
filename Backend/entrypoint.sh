#!/bin/bash


# Run DB migrations
alembic init

mv alembic.example.ini alembic.ini
mv alembic.env.example.py alembic/env.py

alembic revision --autogenerate -m "Tables added"

alembic upgrade head

# Start application
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
