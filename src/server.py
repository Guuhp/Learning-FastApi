from typing import List

from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import create_db, get_db
from src.infra.sqlalchemy.repositories.product import RepositoriesProduct
from src.schemas import schemas

create_db()
app = FastAPI()


@app.post('/product', status_code=status.HTTP_201_CREATED, response_model=schemas.ProductSimple)
def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    product_created = RepositoriesProduct(db).create(product)
    return product_created


@app.get('/products',
         status_code=status.HTTP_200_OK,
         response_model=List[schemas.Product])
def list_products(db: Session = Depends(get_db)):
    products = RepositoriesProduct(db).list_products()
    return products
