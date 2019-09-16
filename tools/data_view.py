#Title: data_view.py
#Project: Chalokwa Battery Analysis
#Author: Lane D. Smith
#Date Last Edited: August 14, 2019

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters


def movingaverage(interval, window_size):
    window= np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')


#Register matplotlib converters
register_matplotlib_converters()

#Load the DataFrames
pv_generation = pd.read_pickle('pv_generation.pkl')
battery_voltage = pd.read_pickle('battery_voltage.pkl')
battery_current = pd.read_pickle('battery_current.pkl')
inverter_power = pd.read_pickle('inverter_power.pkl')
ambient_temperature = pd.read_pickle('ambient_temperature.pkl')
freezer_temperature = pd.read_pickle('freezer_temperature.pkl')

#Determine energy into the inverter
inverter_energy = pd.DataFrame(data = inverter_power['Power into Inverter (W)'].values/60, columns = ['Energy into Inverter (Wh)'], index = battery_voltage.index)

#Determine the power charging and discharging from the battery
bat_current = battery_current.values
bat_voltage = battery_voltage.values
pcha = np.zeros((np.size(bat_voltage), 1))
pdis = np.zeros((np.size(bat_voltage), 1))
for i in range(len(bat_voltage)):
    if bat_current[i, 0] > 0:
        pdis[i, 0] = bat_current[i, 0]*bat_voltage[i, 0]
    elif bat_current[i, 0] < 0:
        pcha[i, 0] = bat_current[i, 0]*bat_voltage[i, 0]
    elif np.isnan(bat_current[i, 0]) or np.isnan(bat_voltage[i, 0]):
        pcha[i, 0] = bat_current[i, 0]*bat_voltage[i, 0]
        pdis[i, 0] = bat_current[i, 0]*bat_voltage[i, 0]
    else:
        pass

pcha = pd.DataFrame(data = -1*pcha, columns = ['Battery Charge Power (W)'], index = battery_voltage.index)
pdis = pd.DataFrame(data = -1*pdis, columns = ['Battery Discharge Power (W)'], index = battery_voltage.index)

#Plot a histogram showing the ambient temperature data vs. the CDF
fig, ax = plt.subplots()
ax2 = ax.twinx()
amb_temp = pd.DataFrame(data = ambient_temperature['Ambient Temperature (C)'].values[122400:648000], columns = ['Ambient Temperature (C)'])
nbins = amb_temp['Ambient Temperature (C)'].nunique()
ax.hist(amb_temp['Ambient Temperature (C)'], bins = nbins, density = False)
ax2.hist(amb_temp['Ambient Temperature (C)'], bins = nbins, density = True, cumulative = True, histtype = 'step', color = 'orange')
ax.set_xlim((ax.get_xlim()[0], amb_temp['Ambient Temperature (C)'].max()))
ax.set_xlabel('Ambient Temperature (C)')
ax.set_ylabel('Counts')
ax2.set_ylabel('Cumulative Probability')
plt.grid(True)

#Plot the battery discharge power data vs. the freezer temperature
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.plot(inverter_power['Power into Inverter (W)'])
ax2.plot(freezer_temperature['Freezer Temperature (C)'], color = 'orange')
ax.set_xlabel('Date/Time')
ax.set_ylabel('Power (W)')
ax2.set_ylabel('Temperature (C)')
plt.grid(True)

#Plot the power into the inverter data
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.plot(pcha['Battery Charge Power (W)'], label = 'Battery Charge Power')
ax.plot(-1*pdis['Battery Discharge Power (W)'], color = 'red', label = 'Battery Discharge Power')
ax2.plot(battery_voltage['Battery Voltage (V)'], color = 'orange', label = 'Battery Voltage')
ax.set_xlabel('Date/Time')
ax.set_ylabel('Power (W)')
ax2.set_ylabel('Voltage (V)')
fig.legend()
plt.grid(True)

#Plot the power into the inverter data vs. the battery voltage
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.plot(inverter_power['Power into Inverter (W)'])
ax.hlines(y = 0, xmin = pdis.index.min(), xmax = pdis.index.max(), color = 'red')
ax.plot(pdis.index, movingaverage(inverter_power['Power into Inverter (W)'], 96), color = 'green')
ax2.plot(battery_voltage['Battery Voltage (V)'], color = 'orange')
ax.set_xlabel('Date/Time')
ax.set_ylabel('Power (W)')
ax2.set_ylabel('Voltage (V)')
ax.grid(True)

#Plot the PV generation
fig, ax = plt.subplots()
ax.plot(battery_voltage['Battery Voltage (V)'])
ax.set_xlabel('Date/Time')
ax.set_ylabel('Voltage (V)')
ax.grid(True)

#Display all the plots
plt.show()