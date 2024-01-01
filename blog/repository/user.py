from fastapi import HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, hashing


def create(request: schemas.User, db: Session):
     new_user = models.User(name = request.name, email=request.email, password = hashing.Hash.bcrypt(request.password))
     db.add(new_user)
     db.commit()
     db.refresh(new_user)
     return new_user

def show(id: int, db: Session):
     user = db.query(models.User).filter(models.User.id == id).first()
     if user is None:
          raise HTTPException(status_code=404, detail="User not found")
     return user
