"""functions py file for main"""

import csv
import statistics as s
my_list = []

def get_requirements():
    """prints program requirements"""
    print("Developer: Joshua Mann")
    print("Python Simple Wine Statistics")
    print("\nProgram Requirements:\n"
        + "1. Create wine stats subdirectory with two files: main.py and functions.py."
        + "2. Read \"wine-data.csv\" file.\n"
        + "3. Create user-defined get_range() function.\n"
        + "4. Use Python intrinsic (built-in) functions from \"statistics\" module.\n"
        + "5. Backward-engineer below results.\n")

def get_range(my_list):
    """
    Usage: Calculates range of wine point scores (diff. between min and max)
    Parameters: my_list (use wine-data.csv)
    Returns: Range of wine point scores
    """
    print()
    help(get_range)

    return max(my_list) - min(my_list)

def get_stats_wine():
    """
    Usage: Simple Statistics - Dispersion, Central Tendency, and Variance
        1. call get_range() # returns range of wine point scores
        2. Except for get_range(), remaining stats come from statistics module
    Parameters: none
    Returns: none
    """

    help(get_stats_wine)

    print("Data Dispersion (how data values are spread out):")

    print("{0}{1:,.0f}".format("numbers of items:", len(my_list)))
    print("{0}{1:,.2f}".format("sum:", sum(my_list)))
    print("{0}{1:,.2f}".format("min:", min(my_list)))
    print("{0}{1:,.2f}".format("max:", max(my_list)))
    print("{0}{1:,.2f}".format("range:", range(my_list)))
    print("{0}{1:,.2f}".format("mean:", s.mean(my_list)))
    print("{0}{1:,.2f}".format("median:", s.median(my_list)))
    print("{0}{1:,.2f}".format("mode:", s.mode(my_list)))
    print("{0}{1:,.2f}".format("variance:", s.variance(my_list)))
    print("{0}{1:,.2f}".format("standard deviation:", s.stdev(my_list)))