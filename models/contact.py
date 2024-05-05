from sqlmodel import SQLModel, Field


class Contacts(SQLModel, table=True):
    contact_id: int = Field(primary_key=True, index=True)
    customer_id: int = Field(foreign_key="users.customer_id")
    contact_name: str
    phone: str
    email: str
