import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import make_url

# ==================================================
# DBアクセス
# ==================================================
# ベースクラスの定義
Base = declarative_base()


def _build_database_url() -> str:
  """
  環境変数が無い場合でも動作するようにDB URLを組み立てる。
  末尾にスラッシュが無ければ付与してからファイル名を連結し、
  SQLiteの場合はディレクトリを自動作成する。
  """
  base_url = os.getenv("DATABASE_URL") or "sqlite+aiosqlite:///./db"
  if not base_url.endswith("/"):
    base_url += "/"

  return f"{base_url}memodb.sqlite"


# データベースのURL
DATABASE_URL = _build_database_url()

# 非同期エンジンの作成
engine = create_async_engine(DATABASE_URL, echo=True)

# 非同期セッションの設定
async_session = sessionmaker(
  engine,
  expire_on_commit=False,
  class_=AsyncSession
)

# DBとのセッションを非同期的に扱うことができる関数
async def get_dbsession():
  async with async_session() as session:
    yield session
