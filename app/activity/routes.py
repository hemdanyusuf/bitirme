from flask import Blueprint, request, jsonify
from app.models import db, Activity

activity_bp = Blueprint('activity', __name__)

@activity_bp.route('/', methods=['GET'])
def list_activity():
    records = Activity.query.all()
    return jsonify([{
        'id': r.id,
        'type': r.type,
        'duration_min': r.duration_min,
        'calories_burned': r.calories_burned,
        'timestamp': r.timestamp.isoformat()
    } for r in records])

@activity_bp.route('/', methods=['POST'])
def add_activity():
    data = request.get_json()
    rec = Activity(**data)
    db.session.add(rec)
    db.session.commit()
    return jsonify({'id': rec.id}), 201
