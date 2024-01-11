from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import databases
import sqlalchemy as db

app = FastAPI()

# In memory db (dictionary)
db = {}

###### This does not work because FastAPI uses Pydantic (below)
# class Item: 
#     def __init__(self, item: str, qty: int):
#         self.item = item
#         self.qty = qty

class Item(BaseModel):
    item: str
    qty: int

# Post request to add item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    item_id = str(len(db) + 1)
    db[item_id] = item.dict()
    return {**item.dict(), "id": item_id}

# Get request to get all items
@app.get("/getallitems", response_model=Dict[str, Any])
def get_all_items():
    return db

@app.get("/")
def read_root():
    return {"Hello": "World"}