import asyncio
from .db import engine, Base
from .models import memo  # noqa: F401 model読み込みでmetadataを登録（副作用目的）

# データベースの初期化
async def init_db():
  print("=== データベースの初期化を開始 ===")
  async with engine.begin() as conn:
    # 既存のテーブルを削除
    await conn.run_sync(Base.metadata.drop_all)
    print(">>> 既存のテーブルを削除しました。")
    # テーブルを作成
    await conn.run_sync(Base.metadata.create_all)
    print(">>> 新しいテーブルを作成しました。")

# スクリプトで実行時のみ実行
if __name__ == "__main__":
  asyncio.run(init_db())