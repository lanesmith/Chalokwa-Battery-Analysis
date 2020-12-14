# Title: data_view.py
# Project: Chalokwa Battery Analysis
# Author: Lane D. Smith
# Date Last Edited: December 14, 2020

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd
from pandas.plotting import register_matplotlib_converters


def movingaverage(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, "same")


# Register matplotlib converters
register_matplotlib_converters()

# LaTeX font for plots
rc("font", **{"family": "serif", "serif": ["Computer Modern Roman"]})
## for Palatino and other serif fonts use:
# rc('font',**{'family':'serif','serif':['Palatino']})
# rc('text', usetex = True)

# Load the DataFrames
pv_generation = pd.read_pickle("../data/pv_generation.pkl")
battery_voltage = pd.read_pickle("../data/battery_voltage.pkl")
battery_current = pd.read_pickle("../data/battery_current.pkl")
inverter_power = pd.read_pickle("../data/inverter_power.pkl")
ambient_temperature = pd.read_pickle("../data/ambient_temperature.pkl")
freezer_temperature = pd.read_pickle("../data/freezer_temperature.pkl")

# Determine energy into the inverter
inverter_energy = pd.DataFrame(
    data=inverter_power["Power into Inverter (W)"].values / 60,
    columns=["Energy into Inverter (Wh)"],
    index=battery_voltage.index,
)

# Determine the power charging and discharging from the battery
bat_current = battery_current.values
bat_voltage = battery_voltage.values
pcha = np.zeros((np.size(bat_voltage), 1))
pdis = np.zeros((np.size(bat_voltage), 1))
for i in range(len(bat_voltage)):
    if bat_current[i, 0] > 0:
        pdis[i, 0] = bat_current[i, 0] * bat_voltage[i, 0]
    elif bat_current[i, 0] < 0:
        pcha[i, 0] = bat_current[i, 0] * bat_voltage[i, 0]
    elif np.isnan(bat_current[i, 0]) or np.isnan(bat_voltage[i, 0]):
        pcha[i, 0] = bat_current[i, 0] * bat_voltage[i, 0]
        pdis[i, 0] = bat_current[i, 0] * bat_voltage[i, 0]
    else:
        pass

pcha = pd.DataFrame(
    data=-1 * pcha, columns=["Battery Charge Power (W)"], index=battery_voltage.index
)
pdis = pd.DataFrame(
    data=-1 * pdis, columns=["Battery Discharge Power (W)"], index=battery_voltage.index
)

# Plot instances of interruptions in service
fig, ax = plt.subplots()
# ax2 = ax.twinx()
ax.plot(inverter_power["Power into Inverter (W)"][558000:570000])
ax.set_xlabel("Date")
ax.set_ylabel("Demand (W)")
ax.set_xlim(18060.9, 18068.2)
ax.set_ylim(0, 550)
date_form = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
ax.xaxis.set_major_formatter(date_form)


# Plot power into inverter before June 14th
fig, ax = plt.subplots()
# ax2 = ax.twinx()
ax.plot(inverter_power["Power into Inverter (W)"][520000:525600])
ax.set_xlabel("Date")
ax.set_ylabel("Demand (W)")
# ax2.set_ylabel('Temperature (C)')
ax.set_xlim(737197, 737199)
ax.set_ylim(0, 550)
date_form = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax.xaxis.set_major_formatter(date_form)

# Plot power into inverter after June 14th
fig, ax = plt.subplots()
# ax2 = ax.twinx()
ax.plot(inverter_power["Power into Inverter (W)"][603500:606600])
ax.set_xlabel("Date")
ax.set_ylabel("Demand (W)")
# ax2.set_ylabel('Temperature (C)')
ax.set_xlim(737255, 737257)
ax.set_ylim(0, 550)
date_form = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax.xaxis.set_major_formatter(date_form)

# Plot battery voltage, charging power, and discharging power before June 14th
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.plot(pcha["Battery Charge Power (W)"][520000:525600], label="Charge Power")
ax.plot(
    -1 * pdis["Battery Discharge Power (W)"][520000:525600],
    color="red",
    label="Discharge Power",
)
ax2.plot(
    battery_voltage["Battery Voltage (V)"][520000:525600],
    color="orange",
    label="Voltage",
)
ax.set_xlabel("Date")
ax.set_ylabel("Power (W)")
ax2.set_ylabel("Voltage (V)")
ax.set_xlim(737197, 737199)
ax.set_ylim(0, 1300)
ax2.set_ylim(21.5, 29.5)
date_form = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax.xaxis.set_major_formatter(date_form)
fig.legend()

# Plot battery voltage, charging power, and discharging power after June 14th
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.plot(pcha["Battery Charge Power (W)"][603500:606600], label="Charge Power")
ax.plot(
    -1 * pdis["Battery Discharge Power (W)"][603500:606600],
    color="red",
    label="Discharge Power",
)
ax2.plot(
    battery_voltage["Battery Voltage (V)"][603500:606600],
    color="orange",
    label="Voltage",
)
ax.set_xlabel("Date")
ax.set_ylabel("Power (W)")
ax2.set_ylabel("Voltage (V)")
ax.set_xlim(737255, 737257)
ax.set_ylim(0, 1300)
ax2.set_ylim(21.5, 29.5)
date_form = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax.xaxis.set_major_formatter(date_form)
fig.legend()

# Plot a histogram showing the ambient temperature data vs. the CDF
fig, ax = plt.subplots()
ax2 = ax.twinx()
amb_temp = pd.DataFrame(
    data=ambient_temperature["Ambient Temperature (C)"].values[122400:648000],
    columns=["Ambient Temperature (C)"],
)
nbins = amb_temp["Ambient Temperature (C)"].nunique()
ax.hist(amb_temp["Ambient Temperature (C)"], bins=nbins, density=False)
ax2.hist(
    amb_temp["Ambient Temperature (C)"],
    bins=nbins,
    density=True,
    cumulative=True,
    histtype="step",
    color="orange",
)
ax.set_xlim((ax.get_xlim()[0], amb_temp["Ambient Temperature (C)"].max()))
ax.set_xlabel("Ambient Temperature (C)")
ax.set_ylabel("Counts")
ax2.set_ylabel("Cumulative Probability")


# Plot the battery discharge power data vs. the freezer temperature
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.plot(inverter_power["Power into Inverter (W)"])
ax2.plot(freezer_temperature["Freezer Temperature (C)"], color="orange")
ax.set_xlabel("Date/Time")
ax.set_ylabel("Power (W)")
ax2.set_ylabel("Temperature (C)")
plt.grid(True)


# Plot the battery voltage, charge, and discharge profiles
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.plot(pcha["Battery Charge Power (W)"], label="Battery Charge Power")
ax.plot(
    -1 * pdis["Battery Discharge Power (W)"],
    color="red",
    label="Battery Discharge Power",
)
ax2.plot(
    battery_voltage["Battery Voltage (V)"], color="orange", label="Battery Voltage"
)
ax.set_xlabel("Date/Time")
ax.set_ylabel("Power (W)")
ax2.set_ylabel("Voltage (V)")
fig.legend()
plt.grid(True)

# Plot the power into the inverter data vs. the battery voltage
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.hlines(y=0, xmin=pdis.index.min(), xmax=pdis.index.max(), color="red")
ax.plot(
    pdis.index,
    movingaverage(inverter_power["Power into Inverter (W)"], 96),
    color="green",
)
ax2.plot(battery_voltage["Battery Voltage (V)"], color="orange")
ax.set_xlabel("Date/Time")
ax.set_ylabel("Power (W)")
ax2.set_ylabel("Voltage (V)")
ax.grid(True)

# Plot the battery voltage
fig, ax = plt.subplots()
ax.plot(battery_voltage["Battery Voltage (V)"])
ax.set_xlabel("Date/Time")
ax.set_ylabel("Voltage (V)")
ax.grid(True)

# Plot PV generation
fig, ax = plt.subplots()
ax.plot(pv_generation["PV Generation (W)"])
ax.set_xlabel("Date/Time")
ax.set_ylabel("Power (W)")

# Display all the plots
plt.show()
