from fastapi import APIRouter, Response, status
from app.repository import UserRepository
from app.models import User
from pydantic import BaseModel

router = APIRouter()
repo = UserRepository()


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    birth_date: str | None = None



@router.get("/users")
def list_users():
    return [user.to_dict() for user in repo.get_all_users()]




@router.get("/users/{user_id}")
def get_user_by_id(user_id: int, response: Response):
    user = repo.get_user_by_id(user_id)
    
    if user:
        response.status_code = status.HTTP_200_OK
        return user.to_dict()
    
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "User not found"}



@router.post("/users")
def create_user(user: UserCreate, response: Response):
    new_user = User(name=user.name, email=user.email, password=user.password, birth_date=user.birth_date)
    created_user = repo.add_user(new_user)
    
    if created_user:
        response.status_code = status.HTTP_201_CREATED
        return created_user.to_dict()
    
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "User already exist"}