from flask import Blueprint, request, jsonify
from engine.solve_manager import check_answer
from utils.session_manager import get_session

solve_routes = Blueprint('solve_routes', __name__)

@solve_routes.route('/solve', methods=['POST'])
def solve_puzzle():
    data = request.get_json()
    session_id = data.get('session_id')
    puzzle_type = data.get('puzzle_type')
    user_answer = data.get('answer')

    session = get_session(session_id)
    if not session:
        return jsonify({'error': 'Invalid session'}), 400

    difficulty = session['difficulty']
    is_correct = check_answer(session_id, puzzle_type, user_answer, difficulty)

    return jsonify({'correct': is_correct})
