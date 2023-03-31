from sqlalchemy.orm import Session

from src.infra.sqlalchemy.models import models
from src.schemas import schemas


class RepositoriesProduct():

    def __init__(self, db: Session):
        self.db = db

    def create(self, product: schemas.Product):
        #convertendo schema em um modelo do DB
        db_product = models.Product(name=product.name,
                                    details=product.details,
                                    price=product.price,
                                    available=product.available)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def list_products(self):
        products = self.db.query(models.Product).all()
        return products
