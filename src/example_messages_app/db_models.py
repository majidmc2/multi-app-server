import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from runserver.db_base import Base


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    message = Column(String)
    time = Column(DateTime, default=datetime.datetime.utcnow)
    sender_id = Column(Integer, ForeignKey('user.id'))
    sender = relationship("User", foreign_keys=sender_id)
    receiver_id = Column(Integer, ForeignKey('user.id'))
    receiver = relationship("User", foreign_keys=receiver_id)

    def __init__(self, message, sender, receiver):
        self.message = message
        self.sender = sender
        self.receiver = receiver
