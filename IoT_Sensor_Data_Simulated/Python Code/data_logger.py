import sqlite3
import time
from datetime import datetime
from sensor_simulation import get_sensor_data

def log_data():
    conn = sqlite3.connect('iot_data.db')
    cursor = conn.cursor()

    print("Logging started... Press Ctrl+C to stop.")

    try:
        while True:
            temperature, humidity, gas_level = get_sensor_data()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('INSERT INTO sensor_data (timestamp, temperature, humidity, gas_level) VALUES (?, ?, ?, ?)',
                           (timestamp, temperature, humidity, gas_level))
            conn.commit()
            print(f"Logged: {timestamp} | Temp: {temperature}°C | Humidity: {humidity}% | Gas: {gas_level}ppm")
            time.sleep(5)  # Log every 5 seconds
    except KeyboardInterrupt:
        print("Logging stopped by user.")
    finally:
        conn.close()

if __name__ == "__main__":
    log_data()
