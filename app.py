from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from authentication import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, Token, \
    user_is_admin
from routes import user, book, borrow_return

app = FastAPI()


app.include_router(router=user.router, dependencies=[Depends(user_is_admin)])
app.include_router(book.router)
app.include_router(borrow_return.router)


@app.get("/")
async def root():
    return "ABC Book Club"


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user ID or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user['_id'])},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")
