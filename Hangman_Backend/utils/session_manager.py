import uuid
from utils.word_selector import select_random_word

# In-memory session storage
sessions = {}

def create_session(difficulty='medium'):
    session_id = str(uuid.uuid4())
    word = select_random_word(difficulty)

    sessions[session_id] = {
        'difficulty': difficulty,
        'word': word,
        'revealed_letters': [],
        'puzzles_completed': 0,
        'current_letter_index': 0,
        'failed': False
    }
    return session_id

def get_session(session_id):
    return sessions.get(session_id, None)

def update_session(session_id, key, value):
    if session_id in sessions:
        sessions[session_id][key] = value
        return True
    return False

def reset_session(session_id):
    if session_id in sessions:
        word = get_word(sessions[session_id]['difficulty'])
        sessions[session_id]['word'] = word
        sessions[session_id]['revealed_letters'] = []
        sessions[session_id]['current_letter_index'] = 0
        sessions[session_id]['puzzles_completed'] = 0
        sessions[session_id]['failed'] = False
        return True
    return False

def delete_session(session_id):
    return sessions.pop(session_id, None)

# Utility: Reveal next letter
def reveal_next_letter(session_id):
    session = get_session(session_id)
    if not session:
        return None
    index = session['current_letter_index']
    if index >= len(session['word']):
        return None
    letter = session['word'][index]
    session['revealed_letters'].append(letter)
    session['current_letter_index'] += 1
    session['puzzles_completed'] += 1
    return letter

# Utility: Check if game is complete
def is_game_complete(session_id):
    session = get_session(session_id)
    if not session:
        return False
    return session['current_letter_index'] >= len(session['word'])

# Utility: Change difficulty dynamically
def change_difficulty(session_id, new_difficulty):
    if session_id in sessions:
        sessions[session_id]['difficulty'] = new_difficulty
        return True
    return False
