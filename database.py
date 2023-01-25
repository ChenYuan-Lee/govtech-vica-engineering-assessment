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


# Delete a user from the database
async def delete_user(id: str):
    id_filter = {"_id": ObjectId(id)}
    user = await users_collection.find_one(id_filter)
    if user:
        await users_collection.delete_one(id_filter)
        return True

    return False
