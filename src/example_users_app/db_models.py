from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref

from runserver.db_base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, unique=True)
    name = Column(String, unique=True)
    secret_key = Column(String)
    authenticated = Column(Boolean)
    session_start_time = Column(DateTime)

    def __init__(self, user_id, name, secret_key, authenticated):
        self.user_id = user_id
        self.name = name
        self.secret_key = secret_key
        self.authenticated = authenticated
