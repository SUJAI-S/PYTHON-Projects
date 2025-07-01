import sqlite3

def create_db():
    conn = sqlite3.connect('iot_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL,
            humidity REAL,
            gas_level REAL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database and table created successfully.")

if __name__ == "__main__":
    create_db()
