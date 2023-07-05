from flask import Blueprint,jsonify

main = Blueprint('hello_world',__name__)
@main.route('/',methods=['GET'])
def init():
    return jsonify({"messjage":"Hello World"})