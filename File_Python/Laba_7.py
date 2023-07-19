import pandas as pd

pd.options.display.max_rows = 10

url = 'https://raw.githubusercontent.com/jvns/pandas-cookbook/master/data/popularity-contest'

data = pd.read_csv(url, sep=' ')[:-1]
data.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']
print(data)

print(data.dtypes)
data['atime'] = data['atime'].astype(int)
data['ctime'] = data['ctime'].astype(int)
print(data.dtypes)

data['atime'] = pd.to_datetime(data['atime'], unit='s')
data['ctime'] = pd.to_datetime(data['ctime'], unit='s')
print(data)

data = data[data['atime'] > '1970-01-01']
print(data)

none_lib = data[~data['package-name'].str.contains('lib')]
none_lib.sort_values('ctime', ascending=False, inplace=True)
print(none_lib[:10])

