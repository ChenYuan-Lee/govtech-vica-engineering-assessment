from datetime import datetime

from fastapi import APIRouter, HTTPException

from database import get_book, get_user, update_book
from models.book import BorrowingAvailabilityStatus

router = APIRouter(prefix="/borrow_return", tags=["borrow_return"])


@router.put("/borrow")
async def borrow_book(book_id: str, user_id: str):
    user = await get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} doesn't exist")

    book = await get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book {book_id} doesn't exist")

    if book['borrowing_availability_status'] == BorrowingAvailabilityStatus.UNAVAILABLE.name:
        raise HTTPException(status_code=403, detail=f"Book {book_id} is unavailable for borrowing")

    if user_id in book['borrowed_by']:
        raise HTTPException(status_code=403, detail=f'User {user_id} already borrowed a copy of book {book_id}')

    # add user into the 'borrowed_by' entry
    book['borrowed_by'][user_id] = datetime.utcnow().date()

    remaining_copies = book['total_copies'] - len(book['borrowed_by'])
    if remaining_copies > 0:
        availability_status = BorrowingAvailabilityStatus.AVAILABLE.name
    else:
        availability_status = BorrowingAvailabilityStatus.UNAVAILABLE.name

    book_updated = await update_book(
        id=book_id,
        data={
            'borrowed_by': book['borrowed_by'],
            'borrowing_availability_status': availability_status
        }
    )
    if book_updated:
        return f'User {user_id} successfully borrowed a copy of book {book_id}'


@router.put("/return")
async def return_book(book_id: str, user_id: str):
    user = await get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} doesn't exist")

    book = await get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book {book_id} doesn't exist")

    if user_id not in book['borrowed_by']:
        raise HTTPException(status_code=403, detail=f"User {user_id} did not borrow book {book_id}")

    # remove user
    book['borrowed_by'].pop(user_id)

    book_updated = await update_book(
        id=book_id,
        data={
            'borrowed_by': book['borrowed_by'],
            'borrowing_availability_status': BorrowingAvailabilityStatus.AVAILABLE.name
        }
    )
    if book_updated:
        return f'User {user_id} successfully returned a copy of book {book_id}'
