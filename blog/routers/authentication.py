from fastapi import APIRouter, Depends, HTTPException
from .. import schemas, database, models, hashing, token
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags= ["Authentication"]
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if user is None:
          raise HTTPException(status_code=404, detail=f"Invalid Credentials")
    elif not hashing.Hash.verify(user.password, request.password):
          raise HTTPException(status_code=404, detail=f"Incorrect Passwords")
    #generate a jwt token and return

    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}