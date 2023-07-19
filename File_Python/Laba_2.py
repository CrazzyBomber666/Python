import matplotlib.pyplot as plt
import pandas as pn

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

data = pn.read_csv('/home/exclusive/FileGitHub/LinuxOnWindow/Современные методы/File_data/311-service-requests.csv', \
    sep=',', encoding='latin1')
data_count_complaint_type = data['Complaint Type'].value_counts()
data_count_complaint_type[:10].plot(kind='bar')
plt.show()