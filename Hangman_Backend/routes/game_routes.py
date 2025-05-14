from flask import Blueprint, jsonify, request
from engine.game_engine import GameEngine

game_bp = Blueprint('game', __name__)

# Initialize the game engine
game_engine = GameEngine()

@game_bp.route('/start', methods=['GET'])
def start_game():
    difficulty = request.args.get('difficulty', 'medium')  # Default to 'medium'
    game_engine.difficulty = difficulty
    game_engine.reset_game()
    return jsonify({"message": "Game started", "hidden_word": game_engine.hidden_word, "status": "ok", "difficulty": difficulty})

@game_bp.route('/guess', methods=['POST'])
def guess_letter():
    letter = request.json.get('letter')
    if not letter or len(letter) != 1:
        return jsonify({"message": "Invalid input. Please provide a single letter."}), 400

    result = game_engine.guess(letter.lower())
    return jsonify({"message": result, "hidden_word": game_engine.hidden_word, "status": "ok"})
