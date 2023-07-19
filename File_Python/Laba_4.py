import pandas as pn
import matplotlib.pyplot as plt
import numpy as np

pn.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

"""url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
url = url_template.format(month=3, year=2012)
weather_mar2012 = pn.read_csv(url, parse_dates=True)"""

"""print(weather_mar2012)

weather_mar2012["Temp (°C)"].plot(figsize=(15, 5))
plt.show()"""

"""weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')
#print(weather_mar2012[:5])

weather_mar2012.drop(['Longitude (x)', 'Latitude (y)', 'Station Name', 'Climate ID', 'Year', 'Month', 'Time (LST)'], axis=1, inplace=True)
#print(weather_mar2012[:5])
#weather_mar2012.info()

weather_mar2012['Date/Time (LST)'] = pn.to_datetime(weather_mar2012['Date/Time (LST)'], format='%Y-%m-%d %H:%M:%S')
#weather_mar2012.info()

temperatures = weather_mar2012[['Temp (°C)', 'Date/Time (LST)']].copy()
temperatures.set_index('Date/Time (LST)', inplace=True)
temperatures.loc[:, 'Часы'] = temperatures.index.hour
temperatures.groupby('Часы').aggregate(np.median).plot()
plt.show()"""

"""weather_mar2012.columns = [u'Location x', u'Location y', u'Name Station', u'IDClimate', u'Date/Time (LST)', 
u'Year', u'Month', u'Day', u'Time', u'Temp (C)',
u'Temp Flag', u'Dew Point Temp (C)', u'Dew Point Temp Flag',
u'Rel Hum (%)', u'Rel Hum Flag', u'PrecipAmmount', u'PrecipAmmountFlag',
u'Wind Dir (10s deg)', u'Wind Dir Flag',
u'Wind Spd (km/h)', u'Wind Spd Flag', u'Visibility (km)', u'Visibility Flag', u'Stn Press (kPa)', u'Stn Press Flag', u'Hmdx', u'Hmdx Flag', u'Wind Chill',
u'Wind Chill Flag', u'Weather']"""

def start():
    weather2012 = pn.DataFrame()
    for month in range(1, 13):
        print('Проход:', month)
        weather_month = downoload_weather(year=2012, month=month)
        weather2012 = pn.concat([weather2012, weather_month])
    return weather2012

def downoload_weather(year, month):
    url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
    url = url_template.format(year=year, month=month)
    weather = pn.read_csv(url, parse_dates=True)
    weather = weather.dropna(axis=1, how='any')
    weather.drop(['Longitude (x)', 'Latitude (y)', 'Station Name', 'Climate ID', 'Year', 'Month', 'Time (LST)'], axis=1, inplace=True)
    return weather

def save_to_csv_file(weather):
    weather.to_csv('/home/exclusive/FileGitHub/LinuxOnWindow/Современные методы/Материалы/Weather2012.csv')

def obrabotka(weather):
    weather['Date/Time (LST)'] = pn.to_datetime(weather['Date/Time (LST)'], format='%Y-%m-%d %H:%M:%S')
    temperatures = weather[['Temp (°C)', 'Date/Time (LST)']].copy()
    temperatures.set_index('Date/Time (LST)', inplace=True)
    temperatures.loc[:, 'Часы'] = temperatures.index.hour
    temperatures.groupby('Часы').aggregate(np.median).plot()
    plt.show()

if __name__ == '__main__':
    weather2012 = start()
    save_to_csv_file(weather=weather2012)
    obrabotka(weather=weather2012)

