from app.main import db
from app.main.models.product import Product


def save_data(data):
    db.session.add(data)
    db.session.commit()


def create_product(data):
    store = Product.query.filter_by(name=data['name']).first()
    if not store:
        new_store = Product(**data)
        save_data(new_store)
        return {
            'status': 200,
            'message': 'Product registrado correctamente!'
        }
    else:
        return {
            'status': 406,
            'message': 'El producto ya esta registrado!'
        }


def get_products():
    return Product.query.all()


def get_product(product_id):
    return Product.query.filter_by(product_id=product_id).first()


def delete_product(product_id):
    store = Product.query.filter_by(product_id=product_id).delete()
    db.session.commit()
    return store


def update_product(product_id):
    return Product.query.filter_by(product_id=product_id)
