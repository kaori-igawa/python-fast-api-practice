from fastapi import APIRouter
from typing import Optional
from .service import get_books_by_category

router = APIRouter(prefix="/query_parameter", tags=["query_parameter"])

# クエリパラメータで指定されたカテゴリに基づいて書籍情報を検索し、
# 結果をJSON形式で返す
@router.get("/books/")
async def read_books(category: Optional[str] = None) -> list[dict[str, str]]:
  # クエリパラメータで指定されたカテゴリに基づいて書籍を検索する
  result = get_books_by_category(category)
  # 結果を辞書のリストとして返す
  return [{
    "id": book.id,
    "title": book.title,
    "category": book.category
  } for book in result]