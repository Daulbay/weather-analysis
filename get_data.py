from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import locale
import csv


def main():
    file_path = datetime.now().strftime('%d_%m_%Y.csv')
    locale.setlocale(locale.LC_TIME, 'ru_RU')
    driver = webdriver.Safari()
    driver.get("https://yandex.kz/pogoda/month?lat=43.273564&lon=76.914851&via=hnav")
    time.sleep(3)

    cells = driver.find_elements(By.CLASS_NAME, 'climate-calendar-day')
    weather_data = []
    month_name = ''
    current_year = str(datetime.now().year)
    for cell in cells:
        date_name = cell.find_element(By.CLASS_NAME, 'climate-calendar-day__day').text
        date_parts = date_name.split(' ')
        if len(date_parts) == 2:
            month_name = date_parts[1]
        date_str = date_parts[0] + ' ' + month_name + ' ' + current_year
        date_object = datetime.strptime(date_str, "%d %B %Y")

        temp_day = (cell.find_element(By.CLASS_NAME, 'climate-calendar-day__temp-day').text
                    .replace('+', '')
                    .replace('−', '-'))
        temp_night = (cell.find_element(By.CLASS_NAME, 'climate-calendar-day__temp-night').text
                      .replace('+', '')
                      .replace('−', '-'))

        weather_data.append([date_object.date().strftime('%d.%m.%Y'), int(temp_day), int(temp_night)])
    driver.quit()

    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['day', 'temp_day', 'temp_night'])

        csv_writer.writerows(weather_data)
    return file_path
