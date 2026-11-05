"""functions py file for main"""

import random

def get_requirements():
    """prints program requirements"""
    print("Developer: Joshua Mann")
    print("Pseudo-Random Number Generator")
    print("\nProgram Requirements:\n"
        + "1. Get user beginning and ending integer values, and store in two variables.\n"
        + "2. Display 10 pseudo-random numbers between, and including, above values.\n"
        + "3. Must use integer data types.\n"
        + "4. Example 1: Using range() and randint() functions.\n"
        + "5. Example 2: Using a list with range() and shuffle() functions.\n")

def random_numbers():
    """function prints pseudo-random numbers"""
    # initialize variables
    start = 0
    end = 0

    # get user data
    print("Input:")
    start = int(input("Enter beginning value: "))
    end = int(input("Enter ending value: "))

    # process and output:
    # display 10 random numbers between stard and end, inclusive

    """ print() parameters:
    generic syntax: print(*objects, sep='', end='\n', file=sys.stdout, flush=False)
    objects: object(s) to be printed. * indicates may be more than one object. Multiple comma-separated objects or single object.
    sep: objects separated by sep. default value: ''(space)
    end: printed at last. default: new line character (\n)
    file: must be object with write(string) method. if ommitted, sys.stdout used as default, prints to screen
    flush: if True, stream is forcibly flushed. default value: False
    """

    # range() fnction returns immutable sequence of N numbers, exclusive end value
    # range(start, stop, step) - must be integer numbers
    # note: start (optional, default 0), stop (required, noninclusive), step (optional, default 1)
    # EXAMPLE (hard-coded value, 6): print sequence of numbers from 0 to 5:
    my_sequence = range(6)
    for item in my_sequence:
        print(item)

    # here, using user start/end values
    print("\nOutput:")
    print("Example 1: Using range() and randint() functions:")
    # here, range() used to generate immutable sequence of N numbers, exclusive end value
    # HOWEVER, randint(start, end) used to print range of integers, inclusive
    for item in range(10):
        print(random.randint(start,end), sep=",", end=" ")

    print()

    print("\nExample 2: Using a list, with range() and shuffle() functions:")
    # shuffle() reorganizes order of items in a sequence (e.g., list)
    # range generates range of integers, "end" is noninclusive, must add 1
    # cant use range() by itself, must convert to list
    my_list = list(range(start, end + 1))
    random.shuffle(my_list) # reorganize list item
    for item in my_list:
        print(item, sep=",", end=" ")

    print()