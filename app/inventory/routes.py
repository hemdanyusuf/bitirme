from flask import Blueprint, request, jsonify
from app.models import db, InventoryItem

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/', methods=['GET'])
def list_inventory():
    items = InventoryItem.query.all()
    return jsonify([{
        'id': i.id,
        'name': i.name,
        'quantity': i.quantity,
        'calorie_per_100g': i.calorie_per_100g
    } for i in items])

@inventory_bp.route('/', methods=['POST'])
def add_inventory():
    data = request.get_json()
    item = InventoryItem(**data)
    db.session.add(item)
    db.session.commit()
    return jsonify({'id': item.id}), 201
