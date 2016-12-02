from sqlalchemy import Column, String, Integer
from database import Base


class List(Base):
    __tablename__ = "list"

    id = Column(Integer, primary_key=True)
    book_id = Column(String(20), nullable=False)
    user_id = Column(String(20), index=True, nullable=False)

    def __init__(self, email, book_id, user_id):
        self.email = email
        self.book_id = book_id
        self.user_id = user_id

    def get_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "book_id": self.book_id,
            "user_id": self.user_id
        }

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True)

    def __init__(self, email):
        self.email = email

    def get_dict(self):
        return {
            "id": self.id,
            "email": self.email
        }
