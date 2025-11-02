from fastapi import APIRouter
from app.api.v1 import hello
from app.api.v1.path_parameter import router as path_parameter

api_router = APIRouter()
api_router.include_router(hello.router)
api_router.include_router(path_parameter.router)