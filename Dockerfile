# syntax=docker/dockerfile:1
FROM python:3.12-slim AS builder
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:${PATH}"
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*
# 旧インストールのpoetryがあると邪魔なので掃除（あっても無視）
RUN rm -f /usr/local/bin/poetry || true
# ビルド用にだけ Poetry を入れる
RUN python -m pip install --no-cache-dir pipx && pipx install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock* ./
RUN poetry --version
# ロックから requirements.txt を生成
RUN poetry export -f requirements.txt -o /tmp/requirements.txt --without-hashes

FROM python:3.12-slim AS runtime
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=builder /tmp/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]