# FastAPI × Poetry × Docker スターター

Docker 上で FastAPI を動かし、Poetry で依存管理、VSCode Dev Containers で開発する最小構成です。

## 使い方

1. ZIP を展開してプロジェクト直下へ移動
2. `.env.example` をコピーして `.env` を作成（必要に応じて編集）
3. ビルド & 起動

   ```bash
   docker compose up --build
   ```

- ブラウザで `http://localhost:8000/` にアクセス → `{"status": "ok", "message": "..."}` が返ればOK
- API ドキュメントは `http://localhost:8000/docs`

### VSCode Dev Containers

VSCode に「Dev Containers」拡張を入れ、コマンドパレットから **Dev Containers: Reopen in Container** を実行します。
以後はコンテナ内で Python の補完／Lint／フォーマット／デバッグが動作します。

- デバッグは `.vscode/launch.json` の「FastAPI (uvicorn) in container」を起動
- 開発時は `--reload` でホットリロード有効

### テスト

```bash
docker compose exec api pytest -q
```

## 構成

```
app/
  ├─ __init__.py
  └─ main.py
.devcontainer/
  └─ devcontainer.json
.vscode/
  └─ launch.json
tests/
  └─ test_root.py
Dockerfile
docker-compose.yml
pyproject.toml
.dockerignore
.env.example
```

## メモ
- Poetry の仮想環境は使わず、コンテナ内のグローバルにインストールしています（`virtualenvs.create = false`）。
- 本番運用では `gunicorn` + `uvicorn.workers.UvicornWorker` を推奨。開発は `--reload` で OK。
