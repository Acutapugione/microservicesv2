from pydantic import BaseModel
from fastapi import FastAPI

class Item(BaseModel):
    name: str
    price: float


app = FastAPI()

@app.post("/items")
def update_item(item: Item):
    print(item.model_dump())
    return {"item_name": item.name }