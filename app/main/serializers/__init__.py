from flask_restplus import Namespace, fields


class ProductSerializer:
    api = Namespace('product')
    product = api.model('product', {
        'product_id': fields.String(readonly=True),
        'sku': fields.String(
            description='Sku',
            max_length=30
        ),
        'name': fields.String(
            description='Name',
            min_length=5,
            max_length=20
        ),
        'description': fields.String(
            description='Description',
            min_length=10,
            max_length=40
        ),
        'stock': fields.Integer(
            description='Stock'
        ),
        'price': fields.Fixed(decimals=2),
        'store_id': fields.String
    })


class StoreSerializer:
    api = Namespace('store')
    store = api.model('store', {
        'store_id': fields.String(readonly=True),
        'name': fields.String(
            description='Name',
            min_length=5,
            max_length=20
        ),
        'address': fields.String(
            description='Address',
            max_length=20
        ),
        'phone_number': fields.String(
            description='Phone number',
            min_length=10,
            max_length=15
        ),
        'products': fields.List(
            fields.Nested(
                ProductSerializer.product
            ), readonly=True
        )
    })
