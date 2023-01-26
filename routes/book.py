from fastapi import APIRouter, HTTPException

from database import add_book, delete_book, update_book
from models.book import BookSchema, UpdateBookModel

router = APIRouter(prefix="/book", tags=["book"])


@router.post("/", response_description="Book added into the database")
async def add_book_data(book: BookSchema):
    return await add_book(book)


@router.put("/{id}")
async def update_book_data(id: str, req: UpdateBookModel):
    req = {k: v for k, v in req.dict().items() if v is not None}
    book_updated = await update_book(id, req)
    if book_updated:
        return f"Book {id} updated"
    else:
        raise HTTPException(status_code=404, detail=f"There was an error updating book {id}")


@router.delete("/{id}", response_description="Book data deleted from the database")
async def delete_book_data(id: str):
    book_deleted = await delete_book(id)
    if book_deleted:
        return f"Book {id} deleted successfully"
    else:
        raise HTTPException(status_code=404, detail=f"Book {id} does not exist")
