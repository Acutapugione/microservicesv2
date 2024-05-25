from flask import Flask
from requests import post


app = Flask(__name__)

# class Item(BaseModel):
#     name: str
#     price: float

@app.get("/")
def get_item():
    item = {
        'name': 'vasya',
        'price': 150,
    }
    
    url = "http://backend:8000/items"
    response = post(url=url, json=item).json()
    print(response)
    return response