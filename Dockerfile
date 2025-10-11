# syntax=docker/dockerfile:1
FROM python:3.12-slim AS builder
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:${PATH}" POETRY_NO_INTERACTION=1 POETRY_VIRTUALENVS_CREATE=false
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# Poetry 本体
RUN python -m pip install --no-cache-dir pipx && pipx install poetry
# ★ ここを追加：export コマンドのプラグイン
RUN poetry self add poetry-plugin-export

WORKDIR /app
COPY pyproject.toml poetry.lock* ./

# lock 生成（--no-update は 2.x では不要）
RUN poetry --version && poetry lock

# requirements.txt を生成（export はプラグイン提供）
RUN poetry export -f requirements.txt -o /tmp/requirements.txt --without-hashes

FROM python:3.12-slim AS runtime
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=builder /tmp/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
