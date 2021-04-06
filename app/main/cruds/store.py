from app.main import db
from app.main.models.store import Store


def save_data(data):
    db.session.add(data)
    db.session.commit()


def create_store(data):
    store = Store.query.filter_by(name=data['name']).first()
    if not store:
        new_store = Store(
            name=data['name'],
            address=data['address'],
            phone_number=data['phone_number']
        )
        save_data(new_store)
        return {
            'status': 200,
            'message': 'Tienda registrado correctamente!',
            'data': save_data
        }
    else:
        return {
            'status': 406,
            'message': 'La tienda ya esta registrada!'
        }


def get_stores():
    return Store.query.all()


def get_store(store_id):
    return Store.query.filter_by(store_id=store_id).first()


def delete_store(store_id):
    store = Store.query.filter_by(store_id=store_id).delete()
    db.session.commit()
    return store


def update_store(store_id):
    return Store.query.filter_by(store_id=store_id)
