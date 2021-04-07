from app.main import db
from flask import Response, request
from flask_restplus import Resource

from ..cruds.product import (create_product,
                             delete_product,
                             get_product,
                             get_products,
                             update_product)

from ..serializers import ProductSerializer

api = ProductSerializer.api
product = ProductSerializer.product


@api.route('/')
class ProductCreateAndList(Resource):
    @api.doc('List of stores')
    @api.marshal_list_with(product, envelope='data')
    def get(self):
        return get_products()

    @api.response(200, 'Product created.')
    @api.doc('Create a new product')
    @api.expect(product, validate=True)
    def post(self):
        data = request.json
        return create_product(data=data)


@api.route('/<product_id>')
@api.response(404, 'Product not found')
class Product(Resource):
    @api.doc('Get a product')
    @api.marshal_with(product)
    def get(self, product_id):
        product = get_product(product_id)
        if not product:
            return {
                'status': 404,
                'message': 'Product not found!'
            }
        else:
            return product

    @api.expect(product, validate=True)
    def put(self, product_id):
        product = update_product(product_id)
        if not product:
            api.abort(404)
        product.update(api.payload)
        db.session.commit()

        return {
            'status': 200,
            'message': 'Product updated',
            'data': api.payload
        }

    def delete(self, product_id):
        product = delete_product(product_id)
        if not product:
            return {
                'status': 404,
                'message': 'Product not found!'
            }
        return {
            'status': 404,
            'message': 'Product deleted!'
        }
