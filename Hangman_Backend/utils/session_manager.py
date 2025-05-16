import uuid
from utils.db import get_db_connection
from utils.word_selector import select_random_word


def create_session(age, difficulty):
    session_id = str(uuid.uuid4())
    word = select_random_word(difficulty)

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   INSERT INTO sessions (session_id, age, difficulty, word, current_letter_index, revealed_letters)
                   VALUES (%s, %s, %s, %s, %s, %s)
                   """, (session_id, age, difficulty, word, 0, ''))

    cursor.execute("""
                   INSERT INTO performance (session_id)
                   VALUES (%s)
                   """, (session_id,))

    conn.commit()
    conn.close()
    return session_id


def get_session(session_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM sessions WHERE session_id = %s", (session_id,))
    session = cursor.fetchone()
    conn.close()
    return session


def update_session(session_id, key, value):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"UPDATE sessions SET {key} = %s WHERE session_id = %s"
    cursor.execute(query, (value, session_id))

    conn.commit()
    conn.close()
    return True


def reset_session(session_id):
    word = select_random_word('easy')  # Or use current session's difficulty

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   UPDATE sessions
                   SET word                 = %s,
                       revealed_letters     = '',
                       current_letter_index = 0,
                       failed               = FALSE
                   WHERE session_id = %s
                   """, (word, session_id))

    conn.commit()
    conn.close()
    return True


def delete_session(session_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM performance WHERE session_id = %s", (session_id,))
    cursor.execute("DELETE FROM sessions WHERE session_id = %s", (session_id,))

    conn.commit()
    conn.close()
    return True


def reveal_next_letter(session_id):
    session = get_session(session_id)
    if not session:
        return None

    index = session['current_letter_index']
    if index >= len(session['word']):
        return None

    letter = session['word'][index]
    revealed = session['revealed_letters'] + letter

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   UPDATE sessions
                   SET revealed_letters     = %s,
                       current_letter_index = %s
                   WHERE session_id = %s
                   """, (revealed, index + 1, session_id))

    conn.commit()
    conn.close()
    return letter


def is_game_complete(session_id):
    session = get_session(session_id)
    if not session:
        return False
    return session['current_letter_index'] >= len(session['word'])


def change_difficulty(session_id, new_difficulty):
    return update_session(session_id, 'difficulty', new_difficulty)
