import sqlite3
import pandas as pd
import schedule
import time
from datetime import datetime

def export_to_csv():
    conn = sqlite3.connect('iot_data.db')
    df = pd.read_sql_query("SELECT * FROM sensor_data", conn)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'data_log_{timestamp}.csv'
    df.to_csv(filename, index=False)
    conn.close()
    print(f"Data exported to {filename} at {datetime.now()}")

# Export every 2 minutes (you can change this)
schedule.every(2).minutes.do(export_to_csv)

print("Automated CSV Export Started... Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
