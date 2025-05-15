from flask import Blueprint, jsonify, request
from utils.session_manager import get_session, update_session, create_session
from utils.word_selector import select_random_word

puzzle_bp = Blueprint('puzzle', __name__)

@puzzle_bp.route('/start', methods=['GET'])
def start_puzzle():
    # Create a session with a default difficulty (for now)
    session_id = create_session(difficulty='medium')

    return jsonify({
        "message": "Puzzle session started",
        "session_id": session_id,
        "status": "ok"
    }), 200

@puzzle_bp.route('/puzzle_diff/<session_id>/set_difficulty', methods=['POST'])
def set_difficulty(session_id):
    data = request.get_json()
    age = data.get('age', None)

    if not age:
        return jsonify({'error': 'Age is required to set difficulty'}), 400

    # Set difficulty based on age
    if age < 18:
        difficulty = 'easy'
    elif age < 35:
        difficulty = 'medium'
    else:
        difficulty = 'hard'

    session = get_session(session_id)
    if not session:
        return jsonify({'error': 'Session not found'}), 404

    # Update the difficulty in the session
    update_session(session_id, 'difficulty', difficulty)

    return jsonify({
        "message": f"Difficulty set to {difficulty}",
        "session_id": session_id,
        "difficulty": difficulty
    }), 200

@puzzle_bp.route('/puzzle_session/<session_id>', methods=['GET'])
def get_puzzle(session_id):
    session = get_session(session_id)
    if not session:
        return jsonify({'error': 'Session not found'}), 404

    if session['failed']:
        return jsonify({'error': 'You failed the last puzzle. Please reset or wait for new one.'}), 400

    word = session['word']
    index = session['current_letter_index']

    if index >= len(word):
        return jsonify({'message': 'All puzzles completed!', 'final_word': word}), 200

    return jsonify({
        'puzzle_id': index,
        'hint': f"Puzzle for letter #{index + 1}",
        'attempts': 1,
        'difficulty': session['difficulty']
    }), 200

@puzzle_bp.route('/puzzle_solve/<session_id>/solve', methods=['POST'])
def solve_puzzle(session_id):
    data = request.get_json()
    user_solved = data.get('solved', False)

    session = get_session(session_id)
    if not session:
        return jsonify({'error': 'Session not found'}), 404

    if user_solved:
        index = session['current_letter_index']
        letter = session['word'][index]
        session['revealed_letters'].append(letter)
        session['current_letter_index'] += 1
        return jsonify({
            'message': 'Correct!',
            'revealed_letters': session['revealed_letters']
        }), 200
    else:
        session['failed'] = True
        return jsonify({
            'message': 'Incorrect. Puzzle failed. Game will reset or skip.'
        }), 200
