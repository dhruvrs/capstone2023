import pandas as pd
import datetime
from fredapi import Fred
import matplotlib.pyplot as plt

fred = Fred(api_key = '2fe2206fc044692733de5ca8fa375adf')
weeklyDiesel = fred.get_series('GASDESW')
regGas = fred.get_series("GASREGW")
convGas = fred.get_series("GASREGCOVW")
avgElec = fred.get_series("APU000072610")

pd = weeklyDiesel
print(pd.tail())
plt.plot(weeklyDiesel, color = "blue", linewidth = .7, label = "Diesel")
plt.plot(regGas, color = 'red', linewidth = .7, label = "Regular all formulations gas")
plt.plot(convGas, color = 'green', linewidth = .7, label = "Regular conventional gas")
plt.title("Weekly Retail and Gasoline Prices")
plt.xlabel("Time")
plt.ylabel("Dollars per Gallon")
plt.legend()
plt.show()

plt.plot(avgElec, color = "#e803fc", linewidth = 2)
plt.xlabel("Year")
plt.ylabel("US Dollars")
plt.title("Average Price of Electricity")
plt.show()