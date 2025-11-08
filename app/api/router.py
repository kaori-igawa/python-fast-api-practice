from fastapi import APIRouter
from app.api.v1 import hello
from app.api.v1.path_parameter import router as path_parameter
from app.api.v1.query_parameter import router as query_parameter
from app.api.v1.pydantic import router as pydantic
from app.api.v1.crud_books import router as crud_books

api_router = APIRouter()
api_router.include_router(hello.router)
api_router.include_router(path_parameter.router)
api_router.include_router(query_parameter.router)
api_router.include_router(pydantic.router)
api_router.include_router(crud_books.router)