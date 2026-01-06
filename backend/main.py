from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base, User

Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB セッションを取得する依存関係
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup")
def signup(name: str, email: str, password: str, db: Session = Depends(get_db)):
    user = User(name=name, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created", "user_id": user.id}
