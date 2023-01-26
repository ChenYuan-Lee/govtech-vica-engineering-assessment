from fastapi import FastAPI

from routes import user, book, borrow_return

app = FastAPI()


app.include_router(user.router)
app.include_router(book.router)
app.include_router(borrow_return.router)


@app.get("/")
async def root():
    return "ABC Book Club"
