from flask_restplus import Api
from flask import Blueprint


from .main.endpoints.store_endpoint import api as store_namespace

blueprint = Blueprint('api', __name__)
api = Api(
    blueprint,
    title='Simple API',
    version='1.0'
)
api.add_namespace(store_namespace, path='/v1/store')
