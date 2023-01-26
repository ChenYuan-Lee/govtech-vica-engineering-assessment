from fastapi import FastAPI

from routes import user, book

app = FastAPI()


app.include_router(user.router)
app.include_router(book.router)


@app.get("/")
async def root():
    return "ABC Book Club"
