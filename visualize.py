import matplotlib.pyplot as plt
from db_ops import get_today_usage_summary

def plot_today_usage_pie():
    data = get_today_usage_summary()
    if not data:
        print("No data available to plot.")
        return

    app_names = [item[0] for item in data]
    durations = [item[1] for item in data]

    plt.figure(figsize=(8, 8))
    plt.pie(durations, labels=app_names, autopct='%1.1f%%', startangle=140)
    plt.title("Today's App Usage")
    plt.axis('equal')  # Equal aspect ratio ensures a perfect circle

    plt.savefig("usage_today_pie.png")
    print("Pie chart saved as usage_today_pie.png")
    plt.close()

if __name__ == "__main__":
    plot_today_usage_pie()

