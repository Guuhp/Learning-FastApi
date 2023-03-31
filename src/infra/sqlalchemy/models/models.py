from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str] = None
    name: str
    telephone: str
    My_Products: List[Product]
    My_Vendas: List[Order]
    my_Requests: List[Order]


class Product(BaseModel):
    id: Optional[str] = None
    user:User
    name: str
    details: str
    price: float
    available: bool = False


class Order(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    amount: int
    delivery: bool = True
    address: str
    comments: Optional[str] = 'sem observações'
