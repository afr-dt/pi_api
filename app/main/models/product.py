import uuid
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

from .. import db


class Product(db.Model):
    __tablename__ = "product"

    product_id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    sku = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(40), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    store_id = db.Column(UUID(as_uuid=True), db.ForeignKey('store.store_id'))

    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    def __str__(self):
        return f'Product: {self.product_id} {self.sku}'
