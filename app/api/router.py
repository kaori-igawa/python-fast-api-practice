from fastapi import APIRouter
from .v1 import hello
from .v1.path_parameter.router import router as path_parameter
from .v1.query_parameter.router import router as query_parameter
from .v1.pydantic.router import router as pydantic
from .v1.crud_books.router import router as crud_books
from .v1.pydantic_field.router import router as pydantic_field
from .v1.fastapi_async.router import router as fastapi_async
from .v1.fastapi_router_refactoring.router import api_router  as fastapi_router_refactoring
from .v1.fastapi_di.router import router  as fastapi_di
from .v1.fastapi_memoapp.router import router  as fastapi_memoapp
from .v1.appendix.router import router as appendix

api_router = APIRouter()
api_router.include_router(hello.router)
api_router.include_router(path_parameter)
api_router.include_router(query_parameter)
api_router.include_router(pydantic)
api_router.include_router(crud_books)
api_router.include_router(pydantic_field)
api_router.include_router(fastapi_async)
api_router.include_router(fastapi_router_refactoring)
api_router.include_router(fastapi_di)
api_router.include_router(fastapi_memoapp)
api_router.include_router(appendix)