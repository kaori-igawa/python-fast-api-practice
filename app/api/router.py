from fastapi import APIRouter
from .v1 import hello
from .v1.path_parameter import router as path_parameter
from .v1.query_parameter import router as query_parameter
from .v1.pydantic import router as pydantic
from .v1.crud_books import router as crud_books
from .v1.pydantic_field import router as pydantic_field
from .v1.fastapi_async import router as fastapi_async
from .v1.fastapi_router_refactoring import router  as fastapi_router_refactoring
from .v1.fastapi_di import router  as fastapi_di
from .v1.fastapi_memoapp import router  as fastapi_memoapp

api_router = APIRouter()
api_router.include_router(hello.router)
api_router.include_router(path_parameter.router)
api_router.include_router(query_parameter.router)
api_router.include_router(pydantic.router)
api_router.include_router(crud_books.router)
api_router.include_router(pydantic_field.router)
api_router.include_router(fastapi_async.router)
api_router.include_router(fastapi_router_refactoring.api_router)
api_router.include_router(fastapi_di.router)
api_router.include_router(fastapi_memoapp.router)