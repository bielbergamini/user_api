from app.repository import UserRepository
from app.models import User

repo = UserRepository()
print(repo.get_user_by_id(1))
print(repo.get_user_by_id(999))


# new_user = User(name="Gabriel", email="gabrielbergamini@email.com", password="11111", birth_date="2006-01-01")

# repo.add_user(new_user)



