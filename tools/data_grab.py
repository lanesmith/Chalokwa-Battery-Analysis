# Title: data_grab.py
# Project: Chalokwa Battery Analysis
# Author: Lane D. Smith
# Date Last Edited: December 14, 2020

import numpy as np
import pandas as pd


def pv_generation_data_reader(*args):
    # First pass of .csv file; split by line
    text1 = open("solar_data.csv", "r")
    data1 = text1.read().split("\n")
    text1.close()
    del data1[-1]

    # Second pass of .csv file; split by comma; delete column classifying the data
    data2 = []
    for i in range(len(data1)):
        data2.append(data1[i].split(","))
        del data2[i][0]
        if data2[i][1] == "":
            data2[i][1] = np.nan
        else:
            data2[i][1] = float(data2[i][1])

    # Convert the list to a DataFrame and index with timestamps in the Zambian timezone
    data3 = pd.DataFrame(data=data2, columns=["Date/Time", "PV Generation (W)"])
    data3["Date/Time"] = pd.to_datetime(data3["Date/Time"])
    data3 = data3.set_index("Date/Time", drop=True)
    data3.index.rename("Date/Time", inplace=True)

    return data3


def battery_voltage_data_reader(*args):
    # First pass of .csv file; split by line
    text1 = open("battery_voltage.csv", "r")
    data1 = text1.read().split("\n")
    text1.close()
    del data1[-1]

    # Second pass of .csv file; split by comma; delete column classifying the data
    data2 = []
    for i in range(len(data1)):
        data2.append(data1[i].split(","))
        del data2[i][0]
        if data2[i][1] == "":
            data2[i][1] = np.nan
        else:
            data2[i][1] = float(data2[i][1])

    # Convert the list to a DataFrame and index with timestamps in the Zambian timezone
    data3 = pd.DataFrame(data=data2, columns=["Date/Time", "Battery Voltage (V)"])
    data3["Date/Time"] = pd.to_datetime(data3["Date/Time"])
    data3 = data3.set_index("Date/Time", drop=True)
    data3.index.rename("Date/Time", inplace=True)

    return data3


def battery_current_data_reader(*args):
    # First pass of .csv file; split by line
    text1 = open("battery_current.csv", "r")
    data1 = text1.read().split("\n")
    text1.close()
    del data1[-1]

    # Second pass of .csv file; split by comma; delete column classifying the data
    data2 = []
    for i in range(len(data1)):
        data2.append(data1[i].split(","))
        del data2[i][0]
        if data2[i][1] == "":
            data2[i][1] = np.nan
        else:
            data2[i][1] = float(data2[i][1])

    # Convert the list to a DataFrame and index with timestamps in the Zambian timezone
    data3 = pd.DataFrame(data=data2, columns=["Date/Time", "Battery Current (A)"])
    data3["Date/Time"] = pd.to_datetime(data3["Date/Time"])
    data3 = data3.set_index("Date/Time", drop=True)
    data3.index.rename("Date/Time", inplace=True)

    return data3


def inverter_power_data_reader(*args):
    # First pass of .csv file; split by line
    text1 = open("power_into_inverter.csv", "r")
    data1 = text1.read().split("\n")
    text1.close()
    del data1[-1]

    # Second pass of .csv file; split by comma; delete column classifying the data
    data2 = []
    for i in range(len(data1)):
        data2.append(data1[i].split(","))
        del data2[i][0]
        if data2[i][1] == "":
            data2[i][1] = np.nan
        else:
            data2[i][1] = float(data2[i][1])

    # Convert the list to a DataFrame and index with timestamps in the Zambian timezone
    data3 = pd.DataFrame(data=data2, columns=["Date/Time", "Power into Inverter (W)"])
    data3["Date/Time"] = pd.to_datetime(data3["Date/Time"])
    data3 = data3.set_index("Date/Time", drop=True)
    data3.index.rename("Date/Time", inplace=True)

    return data3


def ambient_temperature_data_reader(*args):
    # First pass of .csv file; split by line
    text1 = open("ambient_temperature.csv", "r")
    data1 = text1.read().split("\n")
    text1.close()
    del data1[-1]

    # Second pass of .csv file; split by comma; delete column classifying the data
    data2 = []
    for i in range(len(data1)):
        data2.append(data1[i].split(","))
        del data2[i][0]
        if data2[i][1] == "":
            data2[i][1] = np.nan
        else:
            data2[i][1] = float(data2[i][1])

    # Convert the list to a DataFrame and index with timestamps in the Zambian timezone
    data3 = pd.DataFrame(data=data2, columns=["Date/Time", "Ambient Temperature (C)"])
    data3["Date/Time"] = pd.to_datetime(data3["Date/Time"])
    data3 = data3.set_index("Date/Time", drop=True)
    data3.index.rename("Date/Time", inplace=True)

    return data3


def freezer_temperature_data_reader(*args):
    # First pass of .csv file; split by line
    text1 = open("freezer_temperature.csv", "r")
    data1 = text1.read().split("\n")
    text1.close()
    del data1[-1]

    # Second pass of .csv file; split by comma; delete column classifying the data
    data2 = []
    for i in range(len(data1)):
        data2.append(data1[i].split(","))
        del data2[i][0]
        if data2[i][1] == "":
            data2[i][1] = np.nan
        else:
            data2[i][1] = float(data2[i][1])

    # Convert the list to a DataFrame and index with timestamps in the Zambian timezone
    data3 = pd.DataFrame(data=data2, columns=["Date/Time", "Freezer Temperature (C)"])
    data3["Date/Time"] = pd.to_datetime(data3["Date/Time"])
    data3 = data3.set_index("Date/Time", drop=True)
    data3.index.rename("Date/Time", inplace=True)

    return data3


# If you haven't already generated the DataFrames, choose option 1; else choose option 2
option = 2
if option == 1:
    # Generate DataFrames of the different data sets
    pv_generation = pv_generation_data_reader()
    battery_voltage = battery_voltage_data_reader()
    battery_current = battery_current_data_reader()
    inverter_power = inverter_power_data_reader()
    ambient_temperature = ambient_temperature_data_reader()
    freezer_temperature = freezer_temperature_data_reader()

    # Save the DataFrames as .pkl files to make the process faster next time
    pv_generation.to_pickle("pv_generation.pkl")
    battery_voltage.to_pickle("battery_voltage.pkl")
    battery_current.to_pickle("battery_current.pkl")
    inverter_power.to_pickle("inverter_power.pkl")
    ambient_temperature.to_pickle("ambient_temperature.pkl")
    freezer_temperature.to_pickle("freezer_temperature.pkl")

elif option == 2:
    pv_generation = pd.read_pickle("pv_generation.pkl")
    battery_voltage = pd.read_pickle("battery_voltage.pkl")
    battery_current = pd.read_pickle("battery_current.pkl")
    inverter_power = pd.read_pickle("inverter_power.pkl")
    ambient_temperature = pd.read_pickle("ambient_temperature.pkl")
    freezer_temperature = pd.read_pickle("freezer_temperature.pkl")

else:
    print("There are only 2 options! Try again!")
