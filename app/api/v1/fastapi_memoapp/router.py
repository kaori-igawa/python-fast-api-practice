from fastapi import APIRouter
from .schemas.memo import InsertAndUpdateMemoSchema, MemoSchema, ResponseSchema


# APIRouterでこのファイル専用のルートをまとめる（prefixでURLの先頭を決める）
router = APIRouter(prefix="/fastapi_memoapp", tags=["fastapi_memoapp"])

# ==================================================
# メモ用のエンドポイント
# ==================================================
# メモ新規登録
@router.post("/memos", response_model=ResponseSchema)
async def create_memo(memo: InsertAndUpdateMemoSchema):
  print(memo)
  return ResponseSchema(message="メモが正常に登録されました")

# メモ情報全件取得
@router.get("/memos", response_model=list[MemoSchema])
async def get_memos_list():
  return [
    MemoSchema(title="タイトル1", description="詳細1", memo_id=1),
    MemoSchema(title="タイトル2", description="詳細2", memo_id=2),
    MemoSchema(title="タイトル3", description="詳細3", memo_id=3)
  ]

# 特定のメモ情報取得
@router.get("/memos/{memo_id}", response_model=MemoSchema)
async def get_memo_detail(memo_id: int):
  return MemoSchema(title="タイトル1", description="詳細1", memo_id=memo_id)

# 特定のメモを更新する
@router.put("/memos/{memo_id}", response_model=ResponseSchema)
async def modify_memo(memo_id: int, memo: InsertAndUpdateMemoSchema):
  print(memo_id, memo)
  return ResponseSchema(message="メモが正常に更新されました")

# 特定のメモを削除する
@router.delete("/memos/{memo_id}", response_model=ResponseSchema)
async def remove_memo(memo_id: int):
  print(memo_id)
  return ResponseSchema(message="メモが正常に削除されました")