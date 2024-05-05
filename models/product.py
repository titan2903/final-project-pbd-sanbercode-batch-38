from sqlmodel import SQLModel, Field


class Products(SQLModel, table=True):
    product_id: int = Field(primary_key=True, index=True)
    product_name: str
    category: str
    sub_category: str
