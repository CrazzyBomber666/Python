import pandas as pd
import sqlite3 as sql

path = 'Современные методы/Материалы/'
path_sql_test = path + 'test.sqlite'
path_sql_weather = path + 'weather_2012.sqlite'
path_weather = path + 'Weather2012.csv'

con = sql.connect(path_sql_weather)
data = pd.read_sql('SELECT * from weather_2012 LIMIT 3', con)
print(data)

data = pd.read_sql('SELECT * from weather_2012 LIMIT 3', con, index_col='id')
print(data)

data = pd.read_sql('SELECT * from weather_2012 LIMIT 3', con, index_col=['id', 'date_time'])
print(data)

data = pd.read_csv(path_weather)
con = sql.connect(path_sql_test)
con.execute('DROP TABLE IF EXISTS weather_2012')
data.to_sql('weather_2012', con)

con = sql.connect(path_sql_test)
data = pd.read_sql('SELECT * from weather_2012', con, index_col='index')
print(data)

con = sql.connect(path_sql_test)
data = pd.read_sql('SELECT * from weather_2012 ORDER BY Weather', con, index_col='index')
print(data)