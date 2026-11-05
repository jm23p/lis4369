"""functions py file for main"""

def get_requirements():
    """prints program requirements"""
    print("Developer: Joshua Mann")
    print("Temperature Conversion Program")
    print("\nProgram Requirements:\n"
        + "1. Program converts user-entered termperatures into Fahrenheit or Celsius scales.\n"
        + "2. Program continues to prompt for user entry until no longer requested.\n"
        + "3. Note: upper or lower case letters permitted. Though, incorrect entries are not permitted.\n"
        + "4. Note: Program does not validate numeric data (optional requirement).\n")

def temperature_conversion():
    """function captures user input, converts and displays temperature values"""
    # initialize variables
    temperature = 0.0
    choice = '' # initialize to space character
    type = '' # initialize to space character

    # get user data
    print("Input:")

    choice = input("Do you want to convert a temperature (y or n)? ").lower()

    # process and output:
    print("\nOutput:")

    # note: only need to capture first character (e.g., yes vs y or Y)
    while (choice[0] == 'y'):
        type = input(
            "Fahrenheit to Celsius? Type \"f\", or Celsius to Fahrenheit? Type \"c\": ").lower()

        # note: again, only need to capture first character first character in string (e.g., Fahrenheit vs. F or f)
        if type[0] == 'f':
            temperature = float(input("Enter temperature in Fahrenheit: "))
            temperature = ((temperature - 32) * 5) / 9
            print("Temperature in Celsius = " + str(temperature))
            choice = input(
                "\nDo you want to convert another temperature (y or n)? ").lower()

        elif type[0] == 'c':
            temperature = float(input("Enter temperature in Celsius: "))
            temperature = (temperature * 9 / 5) + 32
            print("Temperature in Fahrenheit = " + str(temperature))
            choice = input(
                "\nDo you want to convert another temperature (y or n)? ").lower()

        else:
            print("Incorrect entry. Please try again.")
            choice = input(
                "\nDo you want to convert another temperature (y or n)? ").lower()

    print("\nThank you for using our Temperature Conversion Program!")