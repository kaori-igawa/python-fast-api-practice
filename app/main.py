from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from app.api.router import api_router
from app.api.v1.fastapi_memoapp import db as memo_db

@asynccontextmanager
async def lifespan(app: FastAPI):
  # メモアプリ用のテーブルが存在しない場合に作成する
  await memo_db.init_models()
  yield


app = FastAPI(lifespan=lifespan)

# CORS設定
app.add_middleware(
  CORSMiddleware,
  # 許可するオリジンを指定
  allow_origins=["http://127.0.0.1:5500"],
  # 認証情報を含むリクエストを許可
  allow_credentials=True,
  # 許可するHTTPメソッドを指定
  allow_methods=["*"],
  # 許可するHTTPヘッダーを指定
  allow_headers=["*"],
)

# ルーターのマウント
app.include_router(api_router, prefix="/api/v1")
# /api/v1/users, /api/v1/hello が有効になる

# バリデーションエラーのカスタムハンドラ
@app.exception_handler(ValidationError)
async def validation_exception_handler(exc: ValidationError):
  # ValidationErrorが発生した場合にクライアントに返すレスポンス定義
  return JSONResponse(
    # ステータスコード422
    status_code=422,
    # エラーの詳細
    content={
    # Pydanticが提供するエラーのリスト
    "detail": exc.errors(),
    # バリデーションエラーが発生した時の入力データ
    "body": exc.model
  }
)
