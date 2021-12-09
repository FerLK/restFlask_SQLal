from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"msg": "store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"msg": "Store already exists"}
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"msg": "Error"}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'msg': f'Store {name} deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
