from flask import Blueprint, jsonify

puzzle_bp = Blueprint('puzzle', __name__)

@puzzle_bp.route('/start', methods=['GET'])
def start_puzzle():
    return jsonify({"message": "Puzzle started", "status": "ok"})
