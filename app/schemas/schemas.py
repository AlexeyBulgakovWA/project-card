from pydantic import BaseModel


class CardBase(BaseModel):
    name: str
    projectManager: str
    stack: str
    productOwner: str


class CardDetailsModel(CardBase):
    id: int
    name: str
    projectManager: str
    stack: str
    productOwner: str

    class Config:
        orm_mode = True
