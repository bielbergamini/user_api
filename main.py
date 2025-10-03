from app.repository import UserRepository
from app.models import User

repo = UserRepository()
all_users = repo.get_all_users()

for u in all_users:
    print(u)
    print(u.to_dict())

# new_user = User(name="Gabriel", email="gabrielbergamini@email.com", password="11111", birth_date="2006-01-01")

# repo.add_user(new_user)



