from engine.puzzle_manager import get_puzzle_by_type
from utils.session_manager import update_session, get_session
from utils.performance_manager import update_performance

def check_answer(session_id, puzzle_type, user_answer, difficulty):
    puzzle = get_puzzle_by_type(puzzle_type, difficulty)
    correct_answer = puzzle['answer'].strip().lower()
    user_answer = user_answer.strip().lower()

    if user_answer == correct_answer:
        update_performance(session_id, success=True)
        return True
    else:
        update_performance(session_id, success=False)
        update_session(session_id, 'failed', True)
        return False
