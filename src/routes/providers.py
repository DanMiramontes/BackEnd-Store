from flask import Blueprint,jsonify,request
from src.services.ProviderServices import ProviderServices
from src.models.Providers import Providers
main = Blueprint('providers',__name__)

@main.route('/',methods=['GET'])
def index_categories():
       providers = ProviderServices.index_provider()
       if providers is None:
              response = jsonify({"status":"Failer","message":"no content"})
              return response,400
              
       response = jsonify({"status":"OK","data":providers})
       return response,200

@main.route('/<id>',methods=['GET'])
def show_provider(id):
       if id is None:
              response = jsonify({"status":"Failer","message":"id is required"})
              return response,400
       
       provider = ProviderServices.show_provider(id)
       if provider is None:
              response = jsonify({"status":"Failer","message":"category not found"})
              return response,400
       
       response =  jsonify({"status":"OK","data":provider})
       return response,200

@main.route('/',methods=['POST'])
def create_provider():
       name = request.json['name']
       full_address = request.json['full_address']

       if name is None:
              response = jsonify({"status":"Failer","message":"name is requeried"})
              return response,400
       
       if full_address is None:
              response = jsonify({"status":"Failer","message":"full_address is requeried"})
              return response,400

       new_provider = Providers(name, full_address)

       provider = ProviderServices.create_provider(new_provider)
       if provider is None:
              response = jsonify({"status":"Failer","message":"error"})
       response =  jsonify({"status":"CREATE","data":request.json})
       return response,201

@main.route('/<id>',methods=['PUT'])
def update_product(id):
       if id is None:
          response = jsonify({"status":"Failer","message":"id is required"})
          return response,400
         
       name = request.json['name']
       full_address = request.json['full_address']
    
       if name is None:
              response = jsonify({"status":"Failer","message":"name is requeried"})
              return response,400
       
       if full_address is None:
              response = jsonify({"status":"Failer","message":"full_address is requeried"})
              return response,400
       
       update_provider = Providers(name, full_address)
       provider = ProviderServices.update_provider(id, update_provider)
       
       if provider is None:
              response = jsonify({"status":"Failer","message":"error"})

       response =  jsonify({"status":"UPDATE","data":request.json})
       return response,200


@main.route('/<id>',methods=['DELETE'])
def delete_provider(id):
       
       if id is None:
          response = jsonify({"status":"Failer","message":"id is required"})
          return response,400

       provider = ProviderServices.delete_provider(id)

       if provider is None:
          response = jsonify({"status":"Failer","message":"error"})

       response =  jsonify({"status":"Delete","message":f"category con id:{id} eliminado"})
       return response,204