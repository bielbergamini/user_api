from app.repository import UserRepository
from app.models import User

repo = UserRepository()



new_user = User(name="Bianca", email="bianca@email.com", password="222222", birth_date="2005-01-01")

user = repo.get_user_by_id(3) 

user.name = "Higor"
user.email = "higor@email.com"

repo.update_user(user)




