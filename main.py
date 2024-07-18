from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/sklep_sportowy"
mongo = PyMongo(app)
print(mongo)


@app.route('/delete-kategorie/<id>', methods =['DELETE'] )
def delete_product(id):
    product = mongo.db['kategorie'].delete_one({"_id":ObjectId(id)})

    if product.deleted_count == 0:
        return jsonify({
            'message':"nie znalezione produktu o id {id}"

        }),404
    else:
        return jsonify({
            'message': f'Usunięto element o id {id}'
        })