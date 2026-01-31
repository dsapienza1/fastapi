from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/health")
async def health():
    return{"message": "I am UP & Running!"}

#Query parameter
@app.get("/users/{user_name}")
async def get_user(user_name: str):
    return{"Hello: ": user_name}
