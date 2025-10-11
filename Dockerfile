# syntax=docker/dockerfile:1.7
FROM python:3.12-slim

ENV POETRY_VERSION=1.8.3         PYTHONDONTWRITEBYTECODE=1         PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends         curl build-essential &&         rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - &&         ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Copy dependency files first for better cache
COPY pyproject.toml poetry.lock* ./

# Install dependencies into the container (no venv -> global in image)
RUN poetry config virtualenvs.create false &&         poetry install --no-interaction --no-ansi

# Copy application code
COPY app ./app

# Create non-root user and set permissions
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Default command (dev is overridden by docker-compose with --reload)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
