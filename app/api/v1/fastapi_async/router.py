from fastapi import APIRouter
import asyncio
import httpx

router = APIRouter(prefix="/fastapi_async", tags=["fastapi_async"])

# 郵便番号APIを利用する関数
# 郵便番号APIのURLを指定
# （例）郵便番号「7830060」で検索する場合
# https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060
async def fetch_address(zip_code: str):
  async with httpx.AsyncClient() as client:
    response = await client.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zip_code}")
    return response.json()
  
# エンドポイント
@router.get("/")
async def get_addresses():
  zip_codes = [
    '0600000', # 北海道
    '1000001', # 東京
    '9000000' # 沖縄
  ]
  # * → リストやタプルの展開
  return await asyncio.gather(*(fetch_address(zip_code) for zip_code in zip_codes))
