```python
import sqlite3

def setup_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'adminpass')")
    conn.commit()
    conn.close()

def run_challenge():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    username = input("Enter username: ")
    query = f"SELECT * FROM users WHERE username = ?"
    try:
        cursor.execute(query, (username,))
        results = cursor.fetchall()
        print("Login Successful!" if results else "Invalid username.")
    except sqlite3.OperationalError as e:
        print("Error in query:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    setup_database()
    run_challenge()
```
