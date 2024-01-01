from fastapi import FastAPI
from typing import Union
from typing import Optional
import uvicorn
from . import schemas

app = FastAPI()


# use with query parameter
@app.get("/blog")
def read_root(limit = 10, published: bool = True, sort : Optional[str] = None):
      if published:
           return {'data': f'{limit} published blogs list from the db'}
      else:
           return {'data': f'{limit} blogs from the db'}


@app.get("/about")
def about():
     return {'data': 'about page'}

# Order is imported first unpublished due to types.
@app.get("/blog/unpublished")
def unpublished():
     return {'data': 'all unpublished blogs'}

@app.get("/blog/{item_id}/comments")
def comments(item_id: int):
     return {'data': {'1', '2'}}



@app.post("/blog")
def create_blog(request: schemas.Blog):
     return {'data': f"Blog is created with title as {request.title}"}

if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port = 8000)