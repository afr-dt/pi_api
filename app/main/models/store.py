import uuid
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

from .. import db


class Store(db.Model):
    __tablename__ = "store"

    store_id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(40), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())
    products = db.relationship('Product', backref='owner')
