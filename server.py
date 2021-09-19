from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/marketplace")
def main():
    return {"Project Name": "Marketplace"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

