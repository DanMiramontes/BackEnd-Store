from flask import Flask
from src.routes import categories

app = Flask(__name__)

def init_app():
    app.register_blueprint(categories.main, url_prefix='/api/categories')
    return app