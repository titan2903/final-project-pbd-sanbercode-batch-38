from database.config import Base
from sqlalchemy import Column, Integer, String

class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255))
    category = Column(String(255))
    sub_category = Column(String(255))