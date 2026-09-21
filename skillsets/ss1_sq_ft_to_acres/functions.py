"""functions py file for main"""

# number of square feet in an acre (constant)
SQ_FEET_PER_ACRE = 43560

def get_requirements():
    """prints program requirements"""
    print("Developer: Joshua Mann")
    print("Square Feet to Acres")
    print("\nProgram Requirements:\n"
        + "1. Research: number of square feet to acre of land.\n"
        + "2. Must use float data type for user input and calculation.\n"
        + "3. Format and round conversion to two decimal places.\n")

def calculate_sqft_to_acre():
    """accepts 0 args. calculates square feet to acres and prints output"""
    # variables hold (land) tract size and number of acres
    tract_size = 0.0
    acres = 0.0

    # get square feet in tract
    print("Input:")
    tract_size = float(input("Enter square feet: "))
    # calculate acreage
    acres = tract_size / SQ_FEET_PER_ACRE

    # print number of acres
    print("\nOutput:")
    print("{0:,.2f}{1}{2:,.2f}{3}".format(
        tract_size, " square feet = ", acres, " acres"))