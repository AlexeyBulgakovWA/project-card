from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Card(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    projectManager = Column(String, nullable=False)
    stack = Column(String, nullable=False)
    productOwner = Column(String, nullable=False)
