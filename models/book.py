from datetime import date
from enum import Enum
from typing import Optional, Dict

from pydantic import BaseModel


class BorrowingAvailabilityStatus(Enum):
    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'


class BookSchema(BaseModel):
    title: str
    description: str
    genre: str
    author: str
    year_published: int
    borrowing_availability_status: BorrowingAvailabilityStatus
    last_borrower: Optional[str]
    total_copies: int
    borrowed_by: Dict[str, date]

    class Config:
        schema_extra = {
            "example": {
                "title": "Brave New World",
                "description": "This is an outstanding book",
                "genre": "Science Fiction",
                "author": "Adam Smith",
                "year_published": "2001",
                "borrowing_availability_status": "AVAILABLE",
                "last_borrower": None,
                "total_copies": 10,
                "borrowed_by": {},
            }
        }
