from flask import Flask, send_from_directory
from flask_cors import CORS
import webbrowser
import threading
import os

app = Flask(__name__)
CORS(app)

from routes.game_routes import game_bp
from routes.puzzle_routes import puzzle_bp
from routes.session_routes import session_bp
from routes.solve_routes import solve_routes

app.register_blueprint(game_bp, url_prefix="/game")
app.register_blueprint(puzzle_bp, url_prefix="/puzzle")
app.register_blueprint(session_bp, url_prefix='/session')
app.register_blueprint(solve_routes)

# Path to your frontend folder (adjust if needed)
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Hangman_Frontend')

@app.route('/')
def serve_frontend():
    return send_from_directory(FRONTEND_DIR, 'index.html')

from flask import jsonify

@app.route('/session/start', methods=['POST'])
def start_session():
    # your logic here...
    response = {"session_id": "abc123", "status": "started"}
    return jsonify(response)

@app.route('/trapdoor-test', methods=['GET'])
def test_json():
    return jsonify({"message": "Hello, JSON!"})


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(FRONTEND_DIR, path)

def open_browser():
    webbrowser.open_new('http://localhost:5000')

if __name__ == "__main__":
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True)
