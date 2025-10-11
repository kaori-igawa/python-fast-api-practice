from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/ping")
def ping():
    r = requests.get("https://httpbin.org/get", timeout=5)
    return {"ok": r.ok, "ua": r.json()["headers"].get("User-Agent")}