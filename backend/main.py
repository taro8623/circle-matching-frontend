from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SignupRequest(BaseModel):
    email: str
    password: str
    userName: str

@app.post("/signup")
def signup(data: SignupRequest):
    print("受け取ったデータ:", data)
    return {"message": "ok"}

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(data: LoginRequest):
    print("ログイン要求:", data)
    return {"message": "ok"}
