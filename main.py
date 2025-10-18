from app.repository import UserRepository
from app.models import User
from fastapi import FastAPI
from app.routes import router as user_router
 
app = FastAPI()
app.include_router(user_router)






