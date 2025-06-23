import psutil
from datetime import datetime
import time

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
    print(f" Waiting for '{app_name}' to start...")

    start_time = None

    # Step 1: Wait for app to start
    while True:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == app_name:
                start_time = datetime.now()
                print(f"'{app_name}' started at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
                break
        if start_time:
            break
        time.sleep(1)

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
            break
        time.sleep(1)

if __name__ == "__main__":
    list_running_apps()
    
    app_to_track = input("Enter the app name (e.g., chrome.exe): ")
    track_app(app_to_track)
