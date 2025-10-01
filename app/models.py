# app/models.py
class User:
    def __init__(self, name: str, email: str, password: str, birth_date: str = None, id: int = None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.birth_date = birth_date



    def __repr__(self):
        return f'User(id={self.id}, name="{self.name}", email="{self.email}")'



    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "birth_date": self.birth_date
        }
