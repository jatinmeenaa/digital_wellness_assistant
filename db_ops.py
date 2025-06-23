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

def get_today_usage_summary():
    """
    Fetch total usage time per app for today from the database.
    Returns a list of (app_name, total_time_sec).
    """
    conn = get_connection()
    if not conn:
        print("Failed to connect to database.")
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT app_name, SUM(duration_sec) AS total_time
            FROM app_usage_logs
            WHERE log_date = CURDATE()
            GROUP BY app_name
            ORDER BY total_time DESC;
        """)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching usage summary: {e}")
        return []
    finally:
        cursor.close()
        close_connection(conn)
