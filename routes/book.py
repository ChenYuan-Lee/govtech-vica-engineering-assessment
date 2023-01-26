from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from database import add_book
from models.book import BookSchema

router = APIRouter(prefix="/book", tags=["book"])


@router.post("/", response_description="Book added into the database")
async def add_book_data(book: BookSchema):
    book = jsonable_encoder(book)
    new_book = await add_book(book)
    return new_book
