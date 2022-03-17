from itertools import product
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

from productos import products

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong!"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({'products': products})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound)) > 0:
        return jsonify({'product': productFound[0]})
    return jsonify({'message': 'Product not found'})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity'],
    }
    products.append(new_product)
    return jsonify({"message": "product added succesfully", "products": products})

@app.route('/products/<string:product_name>', methods=['POST'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound)) > 0:
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated!",
            "product": productFound[0]
        })
    return jsonify({"message": "Product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if len(productFound) > 0:
        products.remove(productFound)
        return jsonify({
            "message": "product deleted",
            "products": products
        })
    return jsonify({
        "message": "Product not found!"
    })

if __name__ == '__main__':
    app.run(debug=True, port=4000)

