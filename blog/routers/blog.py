from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
     prefix="/blog",
     tags = ["blogs"]
)


# use with query parameter ilk başta main.py içindeydi router içine aldık
@router.get("/", response_model=list[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post("/")
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

# use with query parameter hepsi sql alcemyde var
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)

# use with query parameter
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)

# use with query parameter
@router.get("/{id}", response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)