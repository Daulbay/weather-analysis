import pandas as pd
import matplotlib.pyplot as plt


def main(file_path: str):
    data = pd.read_csv(file_path, parse_dates=['day'], dayfirst=True)
    avg_day_temp = data['temp_day'].mean()
    avg_night_temp = data['temp_night'].mean()

    coldest_day = data[data['temp_day'] == data['temp_day'].min()]
    hottest_day = data[data['temp_day'] == data['temp_day'].max()]

    plt.figure(figsize=(10, 6))

    plt.subplot(1, 2, 1)
    plt.bar(['Day', 'Night'], [avg_day_temp, avg_night_temp], color=['orange', 'blue'])
    plt.title('Average Temperatures')
    plt.xlabel('Time of Day')
    plt.ylabel('Temperature')

    plt.subplot(1, 2, 2)
    plt.plot(data['day'], data['temp_day'], label='Day')
    plt.plot(data['day'], data['temp_night'], label='Night')
    plt.scatter(coldest_day['day'], coldest_day['temp_day'], color='blue', label='Coldest Day')
    plt.scatter(hottest_day['day'], hottest_day['temp_day'], color='red', label='Hottest Day')
    plt.title('Temperatures Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.legend()

    plt.tight_layout()
    plt.show()