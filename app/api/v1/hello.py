from fastapi import APIRouter

router = APIRouter(prefix="/hello", tags=["hello"])

@router.get("")
async def get_hello():
    return {"messege": "Hello World"}
