import sqlite3
from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item need a store id"
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            #return {'name': item.name, 'price': item.price}, 200
            return item.json(), 200
        return {'message': 'item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'msg': f'An item with {name} already exists.'}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save_to_db()

        except:
            return {"MSG": "ERROR INSERTING"}, 500

        return {'msg': f"{name} registered"}, 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'msg': f'{name} deleted'}


    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            try:
                item.price = data['price']
            except:
                return {'msg':'error 500'}, 500
        item.save_to_db()

        return {'msg': f"{name} atualizado"}, 200


class ItemList(Resource):
    def get(self):
        #return {"items": [item.json() for item in ItemModel.query.all()]}
        return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}