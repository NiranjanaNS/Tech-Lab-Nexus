import sqlite3

def run_challenge():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    username = input("Enter username: ")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        print("Login Successful!" if results else "Invalid username.")
    except sqlite3.OperationalError:
        print("Error in query.")

run_challenge()
