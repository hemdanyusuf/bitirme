from flask import Flask
from .models import db
from app.inventory.routes import inventory_bp
from app.activity.routes import activity_bp
from app.recipes.routes import recipes_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    app.register_blueprint(inventory_bp, url_prefix='/api/inventory')
    app.register_blueprint(activity_bp, url_prefix='/api/activity')
    app.register_blueprint(recipes_bp, url_prefix='/api/recipes')

    return app
