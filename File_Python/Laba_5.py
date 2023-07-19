import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 9
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['font.family'] = 'sans-serif'

weather2012 = pd.read_csv('Современные методы/Материалы/Weather2012.csv', \
    parse_dates=True, index_col='Date/Time (LST)')
#print(weather2012)

"""weather2012_description = weather2012['Weather'].copy()
bool_is_snowing = weather2012_description.str.contains('Snow')
print(bool_is_snowing)"""
"""bool_is_snowing.astype(int).plot()
plt.show()"""

"""weather2012['Temp (°C)'].resample('M').median().plot(kind='bar')
plt.show()"""

"""print(bool_is_snowing.astype(int))

print(bool_is_snowing.astype(int).resample('M').mean())
bool_is_snowing.astype(int).resample('M').mean().plot(kind='bar')
plt.show()"""

temperature = weather2012['Temp (°C)'].resample('M').median()
bool_is_snowing = weather2012['Weather'].str.contains('Snow')
snowiness = bool_is_snowing.astype(int).resample('M').mean()
temperature.name = 'Температура'
snowiness.name = 'Частота выпадения снега'

statistica = pd.concat([temperature, snowiness], axis=1)
print(statistica)
statistica.plot(kind='bar', subplots=True)
plt.show()

