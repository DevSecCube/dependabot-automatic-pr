from flask import Blueprint, jsonify, request

from app import db
from app.models import User

bp = Blueprint('main', __name__)

@bp.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'email': user.email,
        'created_at': user.created_at.isoformat()
    } for user in users])

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data or 'email' not in data:
        return jsonify({'error': 'Email required'}), 400
    
    user = User(email=data['email'])
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        'id': user.id,
        'email': user.email,
        'created_at': user.created_at.isoformat()
    }), 201
