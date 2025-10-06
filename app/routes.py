from fastapi import APIRouter, Response, status
from app.repository import UserRepository

router = APIRouter()
repo = UserRepository()

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