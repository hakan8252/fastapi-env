from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id: int, db: Session):
     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
     if blog: 
        db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
        db.commit()
        return 'done'
     
     raise HTTPException(status_code=404, detail='Blog not exist')


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        for key, value in request.dict().items():
            setattr(blog, key, value)
        db.commit()
        return 'Updated successfully'
    raise HTTPException(status_code=404, detail='Blog not found')
    
def show(id: int, db: Session):
     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
     if blog is None:
          raise HTTPException(status_code=404, detail="Blog not found")
     return blog