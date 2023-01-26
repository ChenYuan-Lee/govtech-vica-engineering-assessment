from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from database import add_book, delete_book
from models.book import BookSchema

router = APIRouter(prefix="/book", tags=["book"])


@router.post("/", response_description="Book added into the database")
async def add_book_data(book: BookSchema):
    book = jsonable_encoder(book)
    new_book = await add_book(book)
    return new_book


@router.delete("/{id}", response_description="Book data deleted from the database")
async def delete_book_data(id: str):
    book_deleted = await delete_book(id)
    if book_deleted:
        return f"Book {id} deleted successfully"
    else:
        raise HTTPException(status_code=404, detail=f"Book {id} does not exist")
