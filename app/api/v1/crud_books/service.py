from .schemas import BookSchema, BookResponseSchema

# デモ用のデータベース代わりに使うリスト
# ダミーの書籍情報リスト
books: list[BookResponseSchema] = [
  BookResponseSchema(id=1, title="Python入門", category="technical"),
  BookResponseSchema(id=2, title="はじめてのプログラミング", category="technical"),
  BookResponseSchema(id=3, title="すすむ巨人", category="comics"),
  BookResponseSchema(id=4, title="DBおやじ", category="comics"),
  BookResponseSchema(id=5, title="週刊ダイヤモンド", category="magazine"),
  BookResponseSchema(id=6, title="ザ・社長", category="magazine")
]