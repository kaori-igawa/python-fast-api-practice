from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from app.api.router import api_router

app = FastAPI()
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
