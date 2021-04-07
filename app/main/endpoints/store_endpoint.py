from app.main import db
from flask import request, Response
from flask_restplus import Resource

from ..cruds.store import (create_store, delete_store, get_store, get_stores,
                           update_store)
from ..serializers import StoreSerializer  # , StoreCreateSerializer

api = StoreSerializer.api
store = StoreSerializer.store


@api.route('/')
class StoreCreateAndList(Resource):
    @api.doc('List of stores')
    @api.marshal_list_with(store, envelope='data')
    def get(self):
        return get_stores()

    @api.response(200, 'Store created.')
    @api.doc('Create a new store')
    @api.expect(store, validate=True)
    def post(self):
        data = request.json
        return create_store(data=data)


@api.route('/<store_id>')
@api.response(404, 'Store not found')
class Store(Resource):
    @api.doc('Get a store')
    @api.marshal_with(store)
    def get(self, store_id):
        store = get_store(store_id)
        if not store:
            return {
                'status': 404,
                'message': 'Store not found!'
            }
        else:
            return store

    @api.expect(store, validate=True)
    def put(self, store_id):
        store = update_store(store_id)
        if not store:
            api.abort(404)
        store.update(api.payload)
        db.session.commit()

        return {
            'status': 200,
            'message': 'Store updated',
            'data': api.payload
        }

    def delete(self, store_id):
        store = delete_store(store_id)
        if not store:
            return {
                'status': 404,
                'message': 'Store not found!'
            }
        return {
            'status': 404,
            'message': 'Store deleted!'
        }
