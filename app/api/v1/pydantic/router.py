from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError
from .service import Event, external_data

router = APIRouter(prefix="/pydantic", tags=["pydantic"])

@router.get("/")
async def get_event() -> Event:
  try:
    event = Event(**external_data)
    return event
  except ValidationError as e:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.errors())
# @router.get("/", response_model=Event)
# async def get_event():
#     return Event(**external_data)