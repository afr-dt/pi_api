from flask_restplus import Namespace, fields


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
        )
    })
