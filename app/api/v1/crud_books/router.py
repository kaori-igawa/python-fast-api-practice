from fastapi import APIRouter
from .schemas import BookSchema, BookResponseSchema
from .service import books

router = APIRouter(prefix="/crud_books", tags=["crud_books"])

# ----------------------------------------------------
# 書籍を追加するためのエンドポイント
# 引数：BookSchema
# 戻り値：BookResponseSchema
# ----------------------------------------------------
@router.post("/", response_model=BookResponseSchema)
def create_book(book: BookSchema):
  # 書籍IDを作成
  # defaultはリストがなかったときのためのもの。
  new_book_id = max([book.id for book in books], default=0) + 1
  # 新しい書籍を作成
  # model_dumpはPydanticモデルのインスタンスから辞書形式のデータを生成し、その辞書をキーワード引数展開（アンパック）
  # JavaScriptのスプレッド構文(...)と同じようなかんじ
  new_book = BookResponseSchema(id=new_book_id, **book.model_dump())
  # ダミーデータに追加
  books.append(new_book)
  # 登録書籍データを返す
  return new_book

# ----------------------------------------------------
# 書籍情報を全件取得するエンドポイント
# 引数：なし
# 戻り値：BookResponseSchemaのリスト
# ----------------------------------------------------
@router.get("/", response_model=list[BookResponseSchema])
def read_books():
  # すべての書籍を取得
  return books