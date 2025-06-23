import psutil
from datetime import datetime
import time
from db_ops import insert_usage_log

def list_running_apps():
    print("{:<30} {:<10} {:<20}".format("App Name", "PID", "Start Time"))
    print("-" * 60)

    for proc in psutil.process_iter(['pid', 'name', 'create_time']):
        try:
            name = proc.info['name']
            pid = proc.info['pid']
            start_time = datetime.fromtimestamp(proc.info['create_time']).strftime("%Y-%m-%d %H:%M:%S")
            print(f"{name:<30} {pid:<10} {start_time:<20}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

def track_app(app_name):

    print(f"Tracking '{app_name}'...")

    # Check if app is running right now
    app_running = False
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == app_name:
            app_running = True
            break

    if not app_running:
        print(f"'{app_name}' is not running anymore. Exiting tracking.")
        return

    start_time = datetime.now()
    print(f"Started tracking at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Step 2: Wait for app to close
    while True:
        app_still_running = False
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == app_name:
                app_still_running = True
                break
        if not app_still_running:
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            print(f" '{app_name}' closed at {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f" Total usage time: {int(duration)} seconds")
            # Insert log into database
            insert_usage_log(app_name, start_time, end_time, int(duration))

            break
        time.sleep(1)

def is_app_running(app_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == app_name:
            return True
    return False

if __name__ == "__main__":
    list_running_apps()
    
    app_to_track = input("Enter the app name (e.g., chrome.exe): ")
    track_app(app_to_track)
