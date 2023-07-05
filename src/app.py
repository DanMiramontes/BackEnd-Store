from flask import Flask
from src.routes import hello_world

app = Flask(__name__)

def init_app():
    app.register_blueprint(hello_world.main, url_prefix='/hello')
    return app