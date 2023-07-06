from flask import Blueprint,jsonify,request
from src.services.DetailServices import DetailServices
from src.models.Detail import Order_detail
main = Blueprint('details',__name__)

@main.route('/',methods=['GET'])
def index_detail():
       detail = DetailServices.index_order() 
       if detail is None:
              response = jsonify({"status":"Failer","message":"no content"})
              return response,400
              
       response = jsonify({"status":"OK","data":detail})
       return response,200

@main.route('/<id>',methods=['GET'])
def show_detail(id):
       if id is None:
              response = jsonify({"status":"Failer","message":"id is required"})
              return response,400
              
       detail = DetailServices.show_order(id)
       if detail is None:
              response = jsonify({"status":"Failer","message":" order detail not found"})
              return response,400
       
       response =  jsonify({"status":"OK","data":detail})
       return response,200



@main.route('/',methods=['POST'])
def create_detail():
       order_id = request.json['order_id']
       product_id = request.json['product_id']
       quantity = request.json['quantity']
       total = request.json['total']

       

       if order_id is None:
              response = jsonify({"status":"Failer","message":"id order is required"})
              return response,400
       
       if product_id is None:
              response = jsonify({"status":"Failer","message":"id product is required"})
              return response,400
       
       if total is None:
              response = jsonify({"status":"Failer","message":"total is required"})
              return response,400
       
       if quantity is None:
              response = jsonify({"status":"Failer","message":"total is required"})
              return response,400
    
       new_detail = Order_detail(purchase_order_id=order_id,product_id=product_id,quantity=quantity,total=total) 
       detail = DetailServices.create_detail(new_detail)

       if detail is None:
              response = jsonify({"status":"Failer","message":"error"})
       response =  jsonify({"status":"CREATE","data":request.json})
       return response,201


@main.route('/<id>',methods=['PUT'])
def update_detail(id):
       
       if id is None:
          response = jsonify({"status":"Failer","message":"id is required"})
          return response,400
        
       quantity = request.json['quantity']
       total = request.json['total']

       
       if total is None:
              response = jsonify({"status":"Failer","message":"total is required"})
              return response,400
       
       if quantity is None:
              response = jsonify({"status":"Failer","message":"total is required"})
              return response,400
    
       update_detail = Order_detail(quantity=quantity,total=total) 
       detail = DetailServices.update_detail(id,update_detail)
       
       if detail is None:
              response = jsonify({"status":"Failer","message":"error"})

       response =  jsonify({"status":"UPDATE","data":request.json})
       return response,200

@main.route('/<id>',methods=['DELETE'])
def delete_detail(id):
       if id is None:
          response = jsonify({"status":"Failer","message":"id is required"})
          return response,400

       detail = DetailServices.delete_detail(id)
       if detail is None:
          response = jsonify({"status":"Failer","message":"error"})

       response =  jsonify({"status":"Delete","message":f"order details con id:{id} eliminado"})
       return response,204


