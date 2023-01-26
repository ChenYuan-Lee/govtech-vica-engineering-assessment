import motor.motor_asyncio
from bson import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.book_club

users_collection = database.get_collection("users_collection")
books_collection = database.get_collection("books_collection")
book_copies_collection = database.get_collection("book_copies_collection")


def convert_object_id_to_str(obj):
    if obj:
        obj['_id'] = str(obj['_id'])


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await users_collection.insert_one(user_data)
    new_user = await users_collection.find_one({"_id": user.inserted_id})
    convert_object_id_to_str(new_user)
    return new_user


# Update a user with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    update_result = await users_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": data}
    )
    return update_result.modified_count == 1


# Delete a user from the database
async def delete_user(id: str):
    delete_result = await users_collection.delete_one({"_id": ObjectId(id)})
    return delete_result.deleted_count == 1


async def add_book(book_data: dict) -> dict:
    book = await books_collection.insert_one(book_data)
    new_book = await books_collection.find_one({"_id": book.inserted_id})
    convert_object_id_to_str(new_book)
    return new_book
