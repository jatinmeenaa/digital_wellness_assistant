from tracker import track_app, list_running_apps
from db_ops import get_today_usage_summary
from visualize import plot_today_usage_pie

def print_menu():
    print("\n=== Digital Wellness Assistant ===")
    print("1. List Running Apps")
    print("2. Track App Usage")
    print("3. Show Today's Usage Summary")
    print("4. Show Pie Chart of Today's Usage")
    print("5. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            list_running_apps()

        elif choice == '2':
            app_name = input("Enter the app name to track (e.g., chrome.exe): ").strip()
            track_app(app_name)

        elif choice == '3':
            summary = get_today_usage_summary()
            if summary:
                print("\nToday's App Usage Summary:")
                for app, duration in summary:
                    print(f"{app:<25} {duration} seconds")
            else:
                print("No usage data found for today.")

        elif choice == '4':
            plot_today_usage_pie()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
