from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")
# /api/v1/users, /api/v1/hello が有効になる
