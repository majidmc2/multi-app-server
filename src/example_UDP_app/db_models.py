from sqlalchemy import Column, Integer

from runserver.db_base import Base


class UDP(Base):
    __tablename__ = 'UDP'

    id = Column(Integer, primary_key=True)
