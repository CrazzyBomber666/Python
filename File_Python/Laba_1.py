import matplotlib.pyplot as plt
import pandas as pn

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

data = pn.read_csv('/home/exclusive/FileGutHub/LinuxOnWindow/Современные методы/File_data/bikes.csv', \
    sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
data.plot()
plt.show()
