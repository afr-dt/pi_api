from app.main import db
from flask import Response, request
from flask_restplus import Resource

from ..cruds.product import (create_product, delete_product, get_product,
                             get_products, update_product)
from ..serializers import ProductSerializer

api = ProductSerializer.api
product = ProductSerializer.product


@api.route('/')
class ProductCreateAndList(Resource):
    @api.doc('List of stores')
    @api.marshal_list_with(product, envelope='data')
    def get(self):
        return get_products()

    @api.response(200, 'Store created.')
    @api.doc('Create a new product')
    @api.expect(product, validate=True)
    def post(self):
        data = request.json
        return create_product(data=data)
