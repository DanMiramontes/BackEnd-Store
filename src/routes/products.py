from flask import Blueprint,jsonify,request
from src.services.ProductsServices import ProductsServices
from src.models.Products import Products
main = Blueprint('products',__name__)

@main.route('/',methods=['GET'])
def index_product():
       products =  ProductsServices.index_product()
       if products is None:
              response = jsonify({"status":"Failer","message":"no content"})
              return response,400
              
       response = jsonify({"status":"OK","data":products})
       return response,200


@main.route('/<id>',methods=['GET'])
def show_product(id):
       if id is None:
              response = jsonify({"status":"Failer","message":"id is required"})
              return response,400
              
       product = ProductsServices.show_product(id)
       if product is None:
              response = jsonify({"status":"Failer","message":"category not found"})
              return response,400
       
       response =  jsonify({"status":"OK","data":product})
       return response,200


@main.route('/',methods=['POST'])
def create_product():
       name = request.json['name']
       description = request.json['description']
       category = request.json['category_id']


       if name is None:
              response = jsonify({"status":"Failer","message":"name is requried"})
              return response,400
       
       if description is None:
              response = jsonify({"status":"Failer","message":"description is required"})
              return response,400
       
       if category is None:
              response = jsonify({"status":"Failer","message":"category is required"})
              return response,400
       
       new_product = Products(name,description,category)

       product = ProductsServices.create_product(new_product)
       if product is None:
              response = jsonify({"status":"Failer","message":"error"})
       response =  jsonify({"status":"CREATE","data":request.json})
       return response,201

@main.route('/<id>',methods=['PUT'])
def update_product(id):
       if id is None:
          response = jsonify({"status":"Failer","message":"id is required"})
          return response,400
         
       name = request.json['name']
       description = request.json['description']
       category = request.json['category_id']


       if name is None:
              response = jsonify({"status":"Failer","message":"name is required"})
              return response,400
       
       if description is None:
              response = jsonify({"status":"Failer","message":"description is required"})
              return response,400
       
       if category is None:
              response = jsonify({"status":"Failer","message":"category is required"})
              return response,400
       
       
       update_product = Products(name,description,category)
       product = ProductsServices.update_product(id,update_product)
       
       if product is None:
              response = jsonify({"status":"Failer","message":"error"})

       response =  jsonify({"status":"UPDATE","data":request.json})
       return response,200

@main.route('/<id>',methods=['DELETE'])
def delete_product(id):
       if id is None:
          response = jsonify({"status":"Failer","message":"id is required"})
          return response,400

       product = ProductsServices.delete_product(id)

       if product is None:
          response = jsonify({"status":"Failer","message":"error"})

       response =  jsonify({"status":"Delete","message":f"product con id:{id} eliminado"})
       return response,204