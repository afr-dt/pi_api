import json
import unittest

from app.main import db
from app.test.base import BaseTestCase
from app.main.models.store import Store


def create_store(self):
    return self.client.post(
        '/api/v1/store/',
        data=json.dumps(dict(
            name='7 Eleven',
            address='Av Principal S/N',
            phone_number='0000000000'
        )),
        content_type='application/json'
    )


def get_store_registered():
    return Store.query.first()


def create_product(self, id):
    return self.client.post(
        '/api/v1/product/',
        data=json.dumps(dict(
            sku='CHA-1232-PP',
            name='Papas Fritas',
            description='Papas Fritas...',
            stock=100,
            price=20,
            store_id=id
        )),
        content_type='application/json'
    )


class TestCreates(BaseTestCase):

    def test_create_store(self):
        with self.client:
            response = create_store(self)
            store = get_store_registered()
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 200)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.content_type == 'application/json')

            response_p = create_product(self, str(store.store_id))
            data = json.loads(response_p.data.decode())
            self.assertTrue(data['status'] == 200)
            self.assertEqual(response_p.status_code, 200)
            self.assertTrue(response_p.content_type == 'application/json')
