from utils.db import get_db_connection

def update_performance(session_id, success=True):
    conn = get_db_connection()
    cursor = conn.cursor()

    if success:
        cursor.execute("""
            UPDATE performance
            SET successes = successes + 1
            WHERE session_id = %s
        """, (session_id,))
    else:
        cursor.execute("""
            UPDATE performance
            SET failures = failures + 1
            WHERE session_id = %s
        """, (session_id,))

    conn.commit()
    conn.close()
