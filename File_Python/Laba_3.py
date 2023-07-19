import matplotlib.pyplot as plt
import pandas as pn

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

data = pn.read_csv('/home/exclusive/FileGitHub/LinuxOnWindow/Современные методы/File_data/bikes.csv', \
    sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

data_count_berri_1 = data[['Berri 1']].copy()
print(data_count_berri_1[:5])

print(data_count_berri_1.index)

print(data_count_berri_1.index.day)

print(data_count_berri_1.index.weekday)

data_count_berri_1.loc[:, 'weekday'] = data_count_berri_1.index.weekday
print(data_count_berri_1[:5])

data_count_berri_1_weekday = data_count_berri_1.groupby('weekday').aggregate(sum)
print(data_count_berri_1_weekday)

data_count_berri_1_weekday.index = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
print(data_count_berri_1_weekday)

data_count_berri_1_weekday.plot(kind='bar')
plt.show()
