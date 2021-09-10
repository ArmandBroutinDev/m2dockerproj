from typing import Optional
from sqlalchemy import *
from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def read_root():
    return json.dumps({"id": "michel"})



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return json.dumps({"item_id": item_id, "q": q})
