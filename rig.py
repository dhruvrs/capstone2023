import pandas as pd
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv('C:/Users/dhruv/Documents/School/Capstone/rig count by state.csv')

data['DATE'] = pd.to_datetime(data['DATE'])
print(data)
plt.plot(data['Texas Land'])
plt.show()
