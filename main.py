from app.repository import UserRepository
from app.models import User

repo = UserRepository()

new_user = User(name="Gabriel", email="gabrielbergamini@email.com", password="11111", birth_date="2006-01-01")

repo.add_user(new_user)