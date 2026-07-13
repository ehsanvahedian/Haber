FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app/Backend

# کپی فایل‌های پروژه
COPY pyproject.toml .
COPY . .

# نصب وابستگی‌ها
RUN uv sync

# کپی و تنظیم entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]