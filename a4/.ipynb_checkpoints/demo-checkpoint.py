import pandas as pd
import pandas_datareader as pdr # remote data access for pandas
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt

start = dt.datetime(2016, 1, 1)
# end = dt.datetime(2024, 10, 15)
end = dt.datetime.now() # current date and time
# for "end:" *must* use Python function for current day/time

# read data into pandas dataframe

# multiple series
df = pdr.DataReader(["DJIA", "SP500"], "fred", start, end)

print("\nPrint number of records: ")
print(len(df))

# why is it important to run the following print statement?
# ans: confirms the exact column names (DJIA and SP500), necessary to reference the correct series
# later when plotting or filtering
print(df.columns)

print("\nPrint data frame: ")
print(df) # note: for efficiency, only prints 60 instead of all records

print("\nPrint first five lines: ")
# note: date is lower than the other columns as it is treated as an index
print(df.head())

print("\nPrint last five lines: ")
print(df.tail())

print("\nPrint first 2 lines: ")
print(df.head(2))

print("\nPrint last 2 lines: ")
print(df.tail(2))

# different style
style.use('fivethirtyeight')