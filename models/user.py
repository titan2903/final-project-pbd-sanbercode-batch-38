from database.config import Base
from sqlalchemy import Column, Integer, String

class Users(Base):
    __tablename__ = "users"

    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    postal = Column(String(255))
    password = Column(String(255))