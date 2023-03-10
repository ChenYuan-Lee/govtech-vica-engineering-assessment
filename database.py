import motor.motor_asyncio
from bson import ObjectId
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pymongo.errors import DuplicateKeyError

from models.book import BookSchema

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.book_club

users_collection = database.get_collection("users_collection")
books_collection = database.get_collection("books_collection")


def convert_object_id_to_str(obj):
    if obj:
        obj['_id'] = str(obj['_id'])


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    try:
        user = await users_collection.insert_one(user_data)
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail=f"User ID already exists. Please try another one.")

    return await users_collection.find_one({"_id": user.inserted_id})


# Update a user with a matching ID
async def update_user(id: str, data: dict) -> bool:
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    update_result = await users_collection.update_one(
        {"_id": id},
        {"$set": data},
    )
    return update_result.matched_count == 1


# Delete a user from the database
async def delete_user(id: str) -> bool:
    delete_result = await users_collection.delete_one({"_id": id})
    return delete_result.deleted_count == 1


async def get_user(user_id: str):
    return await users_collection.find_one({"_id": user_id})


async def get_users():
    users = []
    async for user in users_collection.find():
        users.append(user)
    return users


async def add_book(book_data: BookSchema) -> dict:
    book_data = jsonable_encoder(book_data)
    book = await books_collection.insert_one(book_data)
    new_book = await books_collection.find_one({"_id": book.inserted_id})
    convert_object_id_to_str(new_book)
    return new_book


async def update_book(id: str, data: dict) -> bool:
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    data = jsonable_encoder(data)
    update_result = await books_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": data}
    )
    return update_result.modified_count == 1


async def delete_book(id: str) -> bool:
    delete_result = await books_collection.delete_one({"_id": ObjectId(id)})
    return delete_result.deleted_count == 1


async def get_book(book_id: str):
    return await books_collection.find_one({"_id": ObjectId(book_id)})


async def get_books():
    books = []
    async for book in books_collection.find():
        convert_object_id_to_str(book)
        books.append(book)
    return books
