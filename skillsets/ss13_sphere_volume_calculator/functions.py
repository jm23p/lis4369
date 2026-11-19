"""functions py file for main"""
import math

def get_requirements():
    """prints program requirements"""
    print("Developer: Joshua Mann\n")
    print("Sphere Volume Program\n")
    print("\nProgram Requirements:\n"
        + "1. Program calculates sphere volume in liquid U.S. gallons from user-entered diameter value in inches, \nand rounds to two decimal places.\n"
        + "2. Must use Python\'s *built-in* PI and pow() capabilities.\n"
        + "3. Program checks for non-integers, non-numeric values, and nonpositive integers.\n"
        + "4. Program continues to prompt for user entry until no longer requested, prompt accepts upper or lower case letters.\n")

def sphere_volume():
    # initialize variables
    diameter = 0
    volume = 0.0
    gallons = 0.0
    choice = '' # initialize to space character
    # get user data
    print("Input:")

    choice = input("Do you want to calculate a sphere volume (y or n)? ").lower()
    # Process and Output:
    print("\nOutput:")
    """
    TypeError vs ValueError:
    Passing arguments of wrong type (e.g., passing a list when an int is expected) results in a TypeError,
    but passing arguments with wrong value (e.g., a number outside expected boundaries)  results in a ValueError.
    """

    while (choice[0] == 'y'):
        diameter = input("Please enter diameter in inches (positive integers only): ")
        test = True
        while (test == True):
            try:
                # test for integer value, if it isnt, error
                diameter = int(diameter)

                # check for negative values and 0
                if diameter <= 0:
                    raise ValueError

                # must use floating point values to prevent integer division
                volume = (4.0 / 3.0) * math.pi * math.pow(diameter / 2.0, 3)
                gallons = volume / 231 # convert cubic inches into gallons
                print(
                    "\nSphere volume: {0:,.2f} liquid U.S. gallons\n".format(gallons))
                test = False

            except ValueError:
                print("\nNot valid positive integer!")
                diameter = input("Please enter diameter in inches: ")
            continue

        choice = input("Do you want to calculate another sphere volume? ").lower()

    print("\nThank you for using our Sphere Volume Calculator!")