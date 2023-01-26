from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm

from authentication import Token, user_is_admin, user_is_editor, get_access_token
from routes import user, book, borrow_return

app = FastAPI()

app.include_router(router=user.router, dependencies=[Depends(user_is_admin)])
app.include_router(router=book.router, dependencies=[Depends(user_is_editor)])
app.include_router(borrow_return.router)


@app.get("/")
async def root():
    return "ABC Book Club"


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return await get_access_token(form_data)
