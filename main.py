from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
def read_root():
      return {'data': {'name': 'sss'}}


@app.get("/about")
def about():
     return {'data': 'about page'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}