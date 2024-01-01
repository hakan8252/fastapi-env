from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
     prefix="/user", #bunu ekleyince tek tek hepsinin içine yazmana gerek kalmıyor post get
     tags = ["users"]
)

# Create User
@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.create(request, db)

# Create User
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.show(id, db)