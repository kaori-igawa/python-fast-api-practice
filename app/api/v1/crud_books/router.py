from fastapi import APIRouter, HTTPException, status
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

# ----------------------------------------------------
# 書籍情報をidによって1件取得するエンドポイント
# 引数：書籍ID
# 戻り値：BookResponseSchema
# ----------------------------------------------------
@router.get("/{book_id}", response_model=BookResponseSchema)
def read_book(book_id: int):
  for book in books:
    if book.id == book_id:
      return book
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

# ----------------------------------------------------
# idに対応する書籍情報を更新するエンドポイント
# 引数：
# 書籍ID
# BookSchema
# 戻り値：BookResponseSchema
# ----------------------------------------------------
@router.put("/{book_id}", response_model=BookResponseSchema)
def update_book(book_id: int, book: BookSchema):
  # 特定のIDの書籍を更新
  # enumerateはインデックスと要素の両方を取得することができる
  for index, existing_book in enumerate(books):
    if existing_book.id == book_id:
      updated_book = BookResponseSchema(id=book_id, **book.model_dump())
      books[index] = updated_book
      return updated_book
  # 無ければ例外を投げる
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")