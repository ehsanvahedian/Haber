FROM python:3.14-slim

WORKDIR /app

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir psycopg2-binary sqlalchemy alembic "fastapi[standard]"

COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

