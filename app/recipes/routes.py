from flask import Blueprint, request, jsonify
from app.models import db

recipes_bp = Blueprint('recipes', __name__)

# \u00d6rnek model: daha sonra Recipe modeli ve logic ekleyin
@recipes_bp.route('/', methods=['GET'])
def list_recipes():
    return jsonify([])

@recipes_bp.route('/', methods=['POST'])
def add_recipe():
    data = request.get_json()
    # recipe = Recipe(**data)
    # db.session.add(recipe)
    # db.session.commit()
    return jsonify({'status': 'created'}), 201
