from flask import Blueprint
from flask_restplus import Api

from .main.endpoints.store_endpoint import api as store_namespace
from .main.endpoints.product_endpoint import api as product_namespace

blueprint = Blueprint('api', __name__)
api = Api(
    blueprint,
    title='Simple API',
    version='1.0'
)
api.add_namespace(store_namespace, path='/v1/store')
api.add_namespace(product_namespace, path='/v1/product')
