from fastapi import APIRouter
from .routers.categories import router as category_router
from .routers.items import router as item_router


api_router = APIRouter()

# カテゴリ用ルーターを追加
api_router.include_router(category_router)
# 商品用ルーターを追加
api_router.include_router(item_router)