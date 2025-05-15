from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from routes.game_routes import game_bp
from routes.puzzle_routes import puzzle_bp
from routes.session_routes import session_bp
app.register_blueprint(game_bp, url_prefix="/game")
app.register_blueprint(puzzle_bp, url_prefix="/puzzle")
app.register_blueprint(session_bp, url_prefix='/session')

if __name__ == "__main__":
    app.run(debug=True)
