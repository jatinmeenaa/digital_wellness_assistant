import psutil
from datetime import datetime

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

if __name__ == "__main__":
    list_running_apps()
