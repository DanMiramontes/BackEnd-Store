from flask import Flask
from src.routes import categories
from src.routes import products
from src.routes import providers

app = Flask(__name__)

def init_app():
    app.register_blueprint(categories.main, url_prefix='/api/categories')
    app.register_blueprint(products.main, url_prefix='/api/products')
    app.register_blueprint(providers.main, url_prefix='/api/providers')
    return app