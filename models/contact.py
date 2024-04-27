from database.config import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Contacts(Base):
    __tablename__ = "contacts"

    contact_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.customer_id"))
    contact_name = Column(String(255))
    phone = Column(String(255))
    email = Column(String(255))