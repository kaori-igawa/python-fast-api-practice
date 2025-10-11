from fastapi import FastAPI

app = FastAPI(title="FastAPI Poetry Docker Starter")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "hello from FastAPI in Docker with Poetry"}
