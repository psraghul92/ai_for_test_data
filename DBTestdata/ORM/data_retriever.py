from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DBTestdata.ORM.models import Product, ViewProductDetailsV, Supplier
from DBTestdata.database import NORTHWIND_DATABASE


class DataRetriever:
    def __init__(self):
        self.engine = create_engine(f'sqlite:///{NORTHWIND_DATABASE}')
        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()

    def get_product_with_highest_units_in_stock(self) -> list:
        try:
            return [self.session.query(Product).order_by(Product.UnitsInStock.desc()).first().ProductName]
        finally:
            self.close_session()

    def get_list_product_names_based_on_category(self, category_name:str) -> list:
        try:
            result = self.session.query(ViewProductDetailsV).filter(
                ViewProductDetailsV.CategoryName == category_name).all()
            product_names = list()
            for row in result:
                product_names.append(row.ProductName)
            return product_names
        finally:
            self.close_session()

    def get_country_with_most_suppliers(self) -> list:
        try:
            return [self.session.query(Supplier).order_by(Supplier.Country.desc()).first().Country]
        finally:
            self.close_session()

    def close_session(self):
        if self.session is not None:
            self.session.flush()
            self.session.commit()
            self.session.close()

