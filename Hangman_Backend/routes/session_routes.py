from flask import Blueprint, jsonify, request
from utils.session_manager import create_session, get_session, reset_session

session_bp = Blueprint('session', __name__)

@session_bp.route('/session/start', methods=['POST'])
def start_session():
    data = request.get_json()
    difficulty = data.get('difficulty', 'medium')
    session_id = create_session(difficulty)
    return jsonify({'session_id': session_id}), 200

@session_bp.route('/session_status/<session_id>', methods=['GET'])
def session_status(session_id):
    session = get_session(session_id)
    if not session:
        return jsonify({'error': 'Session not found'}), 404
    return jsonify(session), 200

@session_bp.route('/session_reset/<session_id>', methods=['POST'])
def session_reset(session_id):
    success = reset_session(session_id)
    if not success:
        return jsonify({'error': 'Session not found'}), 404
    return jsonify({'message': 'Session reset'}), 200
