from smm.weather import fetch_eto_and_precip
import csv

if __name__ == '__main__':
    lat, lon = -41.3, 174.8
    days = fetch_eto_and_precip(lat, lon)
    with open('weather_sample.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['date','precip_mm','eto_mm'])
        w.writeheader()
        for d in days:
            w.writerow(d)
