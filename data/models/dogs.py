from sqlalchemy import Column, Integer, String
from data.db import Base


class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    breed = Column(String, index=True, unique=True)
    image = Column(String, nullable=True, default=None)