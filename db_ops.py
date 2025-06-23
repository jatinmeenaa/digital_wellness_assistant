from db_config import get_connection, close_connection
from datetime import datetime

def insert_usage_log(app_name, start_time, end_time, duration_sec):
    """
    Inserts a usage log into the app_usage_logs table.
    
    :param app_name: str - Name of the app
    :param start_time: datetime - Usage start time
    :param end_time: datetime - Usage end time
    :param duration_sec: int - Duration in seconds
    """
    conn = get_connection()
    if not conn:
        print("Could not connect to database.")
        return False

    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO app_usage_logs (app_name, start_time, end_time, duration_sec, log_date)
            VALUES (%s, %s, %s, %s, %s)
        """
        log_date = start_time.date()  # Extract date from start_time
        cursor.execute(sql, (app_name, start_time, end_time, duration_sec, log_date))
        conn.commit()
        print("Usage log inserted successfully.")
        return True
    except Exception as e:
        print(f"Error inserting log: {e}")
        return False
    finally:
        cursor.close()
        close_connection(conn)
