from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    email: Optional[str]
    create_at: datetime = datetime.now()


app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return { "item_id": item_id, "q": q}

@app.post("/user", status_code=201)
async def create_user(user: User):
    usuario = user.dict()
    return user.dict()
   