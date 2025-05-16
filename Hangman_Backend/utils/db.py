import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Tanishq@2105',
        database='hangman_game'
    )
