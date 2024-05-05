from sqlmodel import SQLModel, Field


class Profiles(SQLModel, table=True):
    profile_id: int = Field(primary_key=True, index=True)
    image: str
    username: str
    customer_id: int = Field(foreign_key="users.customer_id")
