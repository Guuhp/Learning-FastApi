from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str] = None
    name: str
    telephone: str


class Product(BaseModel):
    id: Optional[str] = None
    name: str
    details: str
    price: float
    available: bool = False
    #sub classe para informar que o schema esta relacionado a um modelo do banco de dados
    class Config:
        orm_mode = True


class ProductSimple(BaseModel):
    id: Optional[str] = None
    name: str
    price: float

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: Optional[str] = None
    user: User
    amount: int
    delivery: bool = True
    address: str
    comments: Optional[str] = 'sem observações'
