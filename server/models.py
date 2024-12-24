from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin


metadata=MetaData()
db=SQLAlchemy(metadata=metadata)

class Product(db.Model,SerializerMixin):
    __tablename__="products"

    id=db.Column(db.Integer,primary_key=True)
    productName=db.Column(db.String,nullable=False)
    description=db.Column(db.String,nullable=False)

    image_url=db.relationship("Images",back_populates="product")


class Images(db.Model,SerializerMixin):
    __tablename__="images"

    id=db.Column(db.Integer,primary_key=True)
    image_url=db.Column(db.String,nullable=False)
    product_id=db.Column(db.Integer,db.ForeignKey("products.id"))

    product=db.relationship("Product",back_populates="image_url")