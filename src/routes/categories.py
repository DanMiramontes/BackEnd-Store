from flask import Blueprint,jsonify,request
from src.services.CategoriesServices import CategoriesService
from src.models.Categories import Categories
main = Blueprint('categories',__name__)

@main.route('/',methods=['GET'])
def index_categories():
       categories =  CategoriesService.index_categories()
       
       if categories is None:
              response = jsonify({"status":"Failer","message":"no content"})
              return response,400
              
       response = jsonify({"status":"OK","data":categories})
       return response,200


@main.route('/<id>',methods=['GET'])
def show_category(id):
       if id is None:
              response = jsonify({"status":"Failer","message":"id is required"})
              return response,400
              
       category = CategoriesService.show_category(int(id))
       if category is None:
              response = jsonify({"status":"Failer","message":"category not found"})
              return response,400
       
       response =  jsonify({"status":"OK","data":category})
       return response,200

@main.route('/',methods=['POST'])
def create_category():
       name = request.json['name']
       description = request.json['description']


       if name is None:
              response = jsonify({"status":"Failer","message":"name is required"})
              return response,400
       
       if description is None:
              response = jsonify({"status":"Failer","message":"description is required"})
              return response,400
       
       new_category = Categories(name,description)
       print(new_category)
       

       category = CategoriesService.create_category(new_category)
       
       if category is None:
              response = jsonify({"status":"Failer","message":"error"})

       response =  jsonify({"status":"CREATE","data":request.json})
       return response,201



@main.route('/<id>',methods=['PUT'])
def update_category(id):
       if id is None:
          response = jsonify({"status":"Failer","message":"id is required"})
          return response,400
         
       name = request.json['name']
       description = request.json['description']


       if name is None:
              response = jsonify({"status":"Failer","message":"name is required"})
              return response,400
       
       if description is None:
              response = jsonify({"status":"Failer","message":"description is required"})
              return response,400
       
       update_category = Categories(name,description)
       category = CategoriesService.update_category(id,update_category)
       
       if category is None:
              response = jsonify({"status":"Failer","message":"error"})

       response =  jsonify({"status":"UPDATE","data":request.json})
       return response,200


@main.route('/<id>',methods=['DELETE'])
def delete_category(id):
       if id is None:
          response = jsonify({"status":"Failer","message":"id is required"})
          return response,400

       category = CategoriesService.delete_category(id)
       print(category)

       if category is None:
          response = jsonify({"status":"Failer","message":"error"})

       response =  jsonify({"status":"Delete","message":f"category con id:{id} eliminado"})
       return response,204