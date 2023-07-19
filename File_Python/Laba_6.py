import pandas as pd
import numpy as np
from os import path

pd.options.display.max_rows = 9

path_ = r'Современные методы/File_data/311-service-requests.csv'
path_ = path.normcase(path_)

data = pd.read_csv(path_)
print(data['Incident Zip'].unique())

na_values = ['NO CLUE', 'N/A', '0']
data = pd.read_csv(path_, na_values=na_values, dtype={'Incident Zip': str})
print(data['Incident Zip'].unique())

rows_with_dephis = data['Incident Zip'].str.contains('-').fillna(False)
print(data[rows_with_dephis]['Incident Zip'])

long_zip_codes = data['Incident Zip'].str.len() > 5
print(data['Incident Zip'][long_zip_codes].unique())
data['Incident Zip'] = data['Incident Zip'].str.slice(0, 5) 

print(data[data['Incident Zip'] == '00000'])

zero_zips = data['Incident Zip'] == '00000'
data.loc[zero_zips, 'Incident Zip'] = np.nan
unique_zips = data['Incident Zip'].unique()
print(unique_zips)

zips = data['Incident Zip']
bool_is_close = zips.str.startswith('0') | zips.str.startswith('1')
bool_is_far = ~(bool_is_close) & zips.notnull()
print(zips[bool_is_far])
print(data[bool_is_far][['Incident Zip', 'Descriptor', 'City']].sort_values('Incident Zip'))

print(data['City'].str.upper().value_counts())

