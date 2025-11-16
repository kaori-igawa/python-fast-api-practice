from fastapi import APIRouter, Depends
from .service import User, get_active_users

# APIRouterでこのファイル専用のルートをまとめる（prefixでURLの先頭を決める）
router = APIRouter(prefix="/fastapi_di", tags=["fastapi_di"])
  
# 「/fastapi_di/active」へのGETリクエストが来たときに呼ばれる関数を登録
@router.get("/active")
async def list_active_users(active_users: list[User] = Depends(get_active_users)):
  # Dependsを使うと、他の関数（ここではget_active_users）が先に実行されて返り値がここに入る
  print('=== 【依存】してデータを取得 ===')
  return active_users
