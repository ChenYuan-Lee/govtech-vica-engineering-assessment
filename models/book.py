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
    last_borrower: Optional[str]
    total_copies: int
    borrowed_by: Dict[str, date]

    @property
    def borrowing_availability_status(self) -> BorrowingAvailabilityStatus:
        if len(self.borrowed_by) < self.total_copies:
            return BorrowingAvailabilityStatus.AVAILABLE
        return BorrowingAvailabilityStatus.UNAVAILABLE

    class Config:
        schema_extra = {
            "example": {
                "title": "Brave New World",
                "description": "This is an outstanding book",
                "genre": "Science Fiction",
                "author": "Adam Smith",
                "year_published": "2001",
                "total_copies": 10,
                # "borrowed_by": ,
                # "borrowing_availability_status": "",
                # "last_borrower": "",
            }
        }
