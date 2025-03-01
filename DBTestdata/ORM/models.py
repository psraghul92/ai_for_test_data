from typing import Optional

from sqlalchemy import Column, DECIMAL, Double, Integer, LargeBinary, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import decimal


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = 'Category'

    Id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    CategoryName: Mapped[Optional[str]] = mapped_column(String(8000))
    Description: Mapped[Optional[str]] = mapped_column(String(8000))


class Customer(Base):
    __tablename__ = 'Customer'

    Id: Mapped[Optional[str]] = mapped_column(String(8000), primary_key=True)
    CompanyName: Mapped[Optional[str]] = mapped_column(String(8000))
    ContactName: Mapped[Optional[str]] = mapped_column(String(8000))
    ContactTitle: Mapped[Optional[str]] = mapped_column(String(8000))
    Address: Mapped[Optional[str]] = mapped_column(String(8000))
    City: Mapped[Optional[str]] = mapped_column(String(8000))
    Region: Mapped[Optional[str]] = mapped_column(String(8000))
    PostalCode: Mapped[Optional[str]] = mapped_column(String(8000))
    Country: Mapped[Optional[str]] = mapped_column(String(8000))
    Phone: Mapped[Optional[str]] = mapped_column(String(8000))
    Fax: Mapped[Optional[str]] = mapped_column(String(8000))


class CustomerCustomerDemo(Base):
    __tablename__ = 'CustomerCustomerDemo'

    Id: Mapped[Optional[str]] = mapped_column(String(8000), primary_key=True)
    CustomerTypeId: Mapped[Optional[str]] = mapped_column(String(8000))


class CustomerDemographic(Base):
    __tablename__ = 'CustomerDemographic'

    Id: Mapped[Optional[str]] = mapped_column(String(8000), primary_key=True)
    CustomerDesc: Mapped[Optional[str]] = mapped_column(String(8000))


class Employee(Base):
    __tablename__ = 'Employee'

    Id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    LastName: Mapped[Optional[str]] = mapped_column(String(8000))
    FirstName: Mapped[Optional[str]] = mapped_column(String(8000))
    Title: Mapped[Optional[str]] = mapped_column(String(8000))
    TitleOfCourtesy: Mapped[Optional[str]] = mapped_column(String(8000))
    BirthDate: Mapped[Optional[str]] = mapped_column(String(8000))
    HireDate: Mapped[Optional[str]] = mapped_column(String(8000))
    Address: Mapped[Optional[str]] = mapped_column(String(8000))
    City: Mapped[Optional[str]] = mapped_column(String(8000))
    Region: Mapped[Optional[str]] = mapped_column(String(8000))
    PostalCode: Mapped[Optional[str]] = mapped_column(String(8000))
    Country: Mapped[Optional[str]] = mapped_column(String(8000))
    HomePhone: Mapped[Optional[str]] = mapped_column(String(8000))
    Extension: Mapped[Optional[str]] = mapped_column(String(8000))
    Photo: Mapped[Optional[bytes]] = mapped_column(LargeBinary)
    Notes: Mapped[Optional[str]] = mapped_column(String(8000))
    ReportsTo: Mapped[Optional[int]] = mapped_column(Integer)
    PhotoPath: Mapped[Optional[str]] = mapped_column(String(8000))


class EmployeeTerritory(Base):
    __tablename__ = 'EmployeeTerritory'

    EmployeeId: Mapped[int] = mapped_column(Integer)
    Id: Mapped[Optional[str]] = mapped_column(String(8000), primary_key=True)
    TerritoryId: Mapped[Optional[str]] = mapped_column(String(8000))


class Order(Base):
    __tablename__ = 'Order'

    EmployeeId: Mapped[int] = mapped_column(Integer)
    Freight: Mapped[decimal.Decimal] = mapped_column(DECIMAL)
    Id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    CustomerId: Mapped[Optional[str]] = mapped_column(String(8000))
    OrderDate: Mapped[Optional[str]] = mapped_column(String(8000))
    RequiredDate: Mapped[Optional[str]] = mapped_column(String(8000))
    ShippedDate: Mapped[Optional[str]] = mapped_column(String(8000))
    ShipVia: Mapped[Optional[int]] = mapped_column(Integer)
    ShipName: Mapped[Optional[str]] = mapped_column(String(8000))
    ShipAddress: Mapped[Optional[str]] = mapped_column(String(8000))
    ShipCity: Mapped[Optional[str]] = mapped_column(String(8000))
    ShipRegion: Mapped[Optional[str]] = mapped_column(String(8000))
    ShipPostalCode: Mapped[Optional[str]] = mapped_column(String(8000))
    ShipCountry: Mapped[Optional[str]] = mapped_column(String(8000))


class OrderDetail(Base):
    __tablename__ = 'OrderDetail'

    OrderId: Mapped[int] = mapped_column(Integer)
    ProductId: Mapped[int] = mapped_column(Integer)
    UnitPrice: Mapped[decimal.Decimal] = mapped_column(DECIMAL)
    Quantity: Mapped[int] = mapped_column(Integer)
    Discount: Mapped[float] = mapped_column(Double)
    Id: Mapped[Optional[str]] = mapped_column(String(8000), primary_key=True)


class Product(Base):
    __tablename__ = 'Product'

    SupplierId: Mapped[int] = mapped_column(Integer)
    CategoryId: Mapped[int] = mapped_column(Integer)
    UnitPrice: Mapped[decimal.Decimal] = mapped_column(DECIMAL)
    UnitsInStock: Mapped[int] = mapped_column(Integer)
    UnitsOnOrder: Mapped[int] = mapped_column(Integer)
    ReorderLevel: Mapped[int] = mapped_column(Integer)
    Discontinued: Mapped[int] = mapped_column(Integer)
    Id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    ProductName: Mapped[Optional[str]] = mapped_column(String(8000))
    QuantityPerUnit: Mapped[Optional[str]] = mapped_column(String(8000))


class ViewProductDetailsV(Base):
    __tablename__ = 'ProductDetails_V'

    Id: Mapped[Optional[int]] = mapped_column(Integer,primary_key=True)
    ProductName: Mapped[Optional[str]] = mapped_column(String(8000))
    SupplierId: Mapped[Optional[int]] = mapped_column(Integer)
    CategoryId: Mapped[Optional[int]] = mapped_column(Integer)
    QuantityPerUnit: Mapped[Optional[str]] = mapped_column(String(8000))
    UnitPrice: Mapped[decimal.Decimal] = mapped_column(DECIMAL)
    UnitsInStock: Mapped[Optional[int]] = mapped_column(Integer)
    UnitsOnOrder: Mapped[Optional[int]] = mapped_column(Integer)
    ReorderLevel: Mapped[Optional[int]] = mapped_column(Integer)
    Discontinued: Mapped[Optional[int]] = mapped_column(Integer)
    CategoryName: Mapped[Optional[str]] = mapped_column(String(8000))
    CategoryDescription: Mapped[Optional[str]] = mapped_column(String(8000))
    SupplierName: Mapped[Optional[str]] = mapped_column(String(8000))
    SupplierRegion: Mapped[Optional[str]] = mapped_column(String(8000))


class Region(Base):
    __tablename__ = 'Region'

    Id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    RegionDescription: Mapped[Optional[str]] = mapped_column(String(8000))


class Shipper(Base):
    __tablename__ = 'Shipper'

    Id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    CompanyName: Mapped[Optional[str]] = mapped_column(String(8000))
    Phone: Mapped[Optional[str]] = mapped_column(String(8000))


class Supplier(Base):
    __tablename__ = 'Supplier'

    Id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    CompanyName: Mapped[Optional[str]] = mapped_column(String(8000))
    ContactName: Mapped[Optional[str]] = mapped_column(String(8000))
    ContactTitle: Mapped[Optional[str]] = mapped_column(String(8000))
    Address: Mapped[Optional[str]] = mapped_column(String(8000))
    City: Mapped[Optional[str]] = mapped_column(String(8000))
    Region_: Mapped[Optional[str]] = mapped_column('Region', String(8000))
    PostalCode: Mapped[Optional[str]] = mapped_column(String(8000))
    Country: Mapped[Optional[str]] = mapped_column(String(8000))
    Phone: Mapped[Optional[str]] = mapped_column(String(8000))
    Fax: Mapped[Optional[str]] = mapped_column(String(8000))
    HomePage: Mapped[Optional[str]] = mapped_column(String(8000))


class Territory(Base):
    __tablename__ = 'Territory'

    RegionId: Mapped[int] = mapped_column(Integer)
    Id: Mapped[Optional[str]] = mapped_column(String(8000), primary_key=True)
    TerritoryDescription: Mapped[Optional[str]] = mapped_column(String(8000))
