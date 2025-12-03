from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from .routers.memo import router as memo_router

# ==================================================
# 起動ファイル
# ==================================================

# APIRouterでこのファイル専用のルートをまとめる（prefixでURLの先頭を決める）
router = APIRouter(prefix="/fastapi_memoapp", tags=["fastapi_memoapp"])

# ルーターのマウント
router.include_router(memo_router)