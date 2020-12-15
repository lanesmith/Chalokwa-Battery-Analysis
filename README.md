[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Chalokwa-Battery-Analysis

## Package Purpose
The purpose of this package is to analyze battery, load, and temperature data from the KiloWatts for Humanity (KWH) solar kiosk
installed in Chalokwa, Zambia. Data analysis is necessary due to a increase in interruptions in service that have been occurring
since the middle of June 2019. The purpose of the data analysis is to see if any causes of failure can be determined and if any
other pertinant information can be gleaned. Results from this analysis were presented to the KWH Microgrid Team; the main take-
away was that the battery system is failing, likely due to a combination high ambient temperature and daily cycling. An increase
in load was observed, but it does not appear to be the cause of the increase in interruptions in service. Rather, the increased
loading appears to simply have hastened the process of notifying that the battery system was failing. The tools and data
contained within this package will allow for similar data analysis. All data was acquired from [KWH's website](http://kw4h.org/?orgId=2).

## Package Contents
`/tools`: Contains the following modules:
- `data_grab.py`: Reads .csv data downloaded from [KWH's website](http://kw4h.org/?orgId=2) and saves them as pickled DataFrames.
- `data_view.py`: Reads the pickled DataFrames and generates various plots, including the listed data sets.

`/data`: Contains pickled DataFrames of the following data:
- Battery Voltage
- Battery Current
- Power into the Inverter
- PV Generation
- Ambient Temperature
- Freezer Temperature

## Software Requirements
To use the included tools, the following software is required:
- Python 3 (it is recommended to use a scientific distribution of Python, such as Anaconda)

The following Python libraries are also required:
- numpy
- pandas
- matplotlib

## Package Usage
To run the included tools, access the directory containing them (`.../Chalokwa-Battery-Analysis/tools/`) from the command line and
run the desired program.
