from pydantic import BaseModel

# PydanticのBaseModelを継承すると、型チェックやバリデーションを自動でやってくれるデータクラスを作れる
class User(BaseModel):
  # ユーザー名（必須）
  username: str
  # アクティブかどうか。ここではデフォルト値Trueにしておく
  is_active: bool = True

# 今回はDBの代わりに、サンプルデータをPythonのリストで用意
users = [
    User(username="太郎", is_active=True),
    User(username="次郎", is_active=False),
    User(username="花子", is_active=True)
]

# アクティブなユーザーだけを取り出す依存関数。Depends経由で呼び出して使う
def get_active_users():
  # リスト内包表記で、is_activeがTrueのユーザーだけを抽出
  active_users = [user for user in users if user.is_active]
  print('=== アクティブなユーザーを取得 ===')
  return active_users
