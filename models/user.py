from sqlmodel import SQLModel, Field


class Users(SQLModel, table=True):
    customer_id: int = Field(primary_key=True, index=True)
    name: str
    city: str
    state: str
    postal: str
    password: str
