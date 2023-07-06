from flask import Blueprint,jsonify,request
from src.services.OrderServices import OrderServices
from src.models.Orders import Orders
main = Blueprint('orders',__name__)


@main.route('/',methods=['GET'])
def index_order():
       orders = OrderServices.index_order()
       if orders is None:
              response = jsonify({"status":"Failer","message":"no content"})
              return response,400
              
       response = jsonify({"status":"OK","data":orders})
       return response,200

@main.route('/<id>',methods=['GET'])
def show_order(id):
       if id is None:
              response = jsonify({"status":"Failer","message":"id is required"})
              return response,400
              
       order = OrderServices.show_order(id)
       if order is None:
              response = jsonify({"status":"Failer","message":"category not found"})
              return response,400
       
       response =  jsonify({"status":"OK","data":order})
       return response,200


@main.route('/',methods=['POST'])
def create_order():
       provider_id = request.json['provider_id']
       total = request.json['total']
       

       if provider_id is None:
              response = jsonify({"status":"Failer","message":"id provider is required"})
              return response,400
       
       if total is None:
              response = jsonify({"status":"Failer","message":"total is required"})
              return response,400
    
       new_order = Orders(provider_id,total)
       order = OrderServices.create_order(new_order)
       if order is None:
              response = jsonify({"status":"Failer","message":"error"})
       response =  jsonify({"status":"CREATE","data":request.json})
       return response,201


@main.route('/<id>',methods=['PUT'])
def update_order(id):
       
       if id is None:
          response = jsonify({"status":"Failer","message":"id is required"})
          return response,400
       
       provider_id = request.json['provider_id']
       total = request.json['total']
       

       if provider_id is None:
              response = jsonify({"status":"Failer","message":"id provider is required"})
              return response,400
       
       if total is None:
              response = jsonify({"status":"Failer","message":"total is required"})
              return response,400
    
       update_order = Orders(provider_id,total)
    
       order = OrderServices.update_order(id,update_order)
       
       if order is None:
              response = jsonify({"status":"Failer","message":"error"})

       response =  jsonify({"status":"UPDATE","data":request.json})
       return response,200

@main.route('/<id>',methods=['DELETE'])
def delete_order(id):
       if id is None:
          response = jsonify({"status":"Failer","message":"id is required"})
          return response,400

       order = OrderServices.delete_order(id)
       if order is None:
          response = jsonify({"status":"Failer","message":"error"})

       response =  jsonify({"status":"Delete","message":f"category con id:{id} eliminado"})
       return response,204