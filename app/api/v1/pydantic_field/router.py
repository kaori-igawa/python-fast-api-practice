from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError
from .service import BookSchema

router = APIRouter(prefix="/pydantic_field", tags=["pydantic_field"])

@router.post("/", response_model=BookSchema)
async def create_book(book: BookSchema):
  return book