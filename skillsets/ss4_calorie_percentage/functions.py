"""functions py file for main"""

def get_requirements():
    """prints program requirements"""
    print("Developer: Joshua Mann")
    print("Calorie Percentage")
    print("\nProgram Requirements:\n"
        + "1. Find calories per grams of fat, carbs, and protein.\n"
        + "2. Calculate percentages.\n"
        + "3. Must use float data types.\n"
        + "4. Format, rt-align numbers, and round to two decimal places.\n")

# IPO: Input > Process > Output
# get user data

def get_user_input():
    """gets user input"""
    # initialize variables
    fat_grams = 0.0
    carb_grams = 0.0
    protein_grams = 0.0
    
    print("Input:")
    fat_grams = float(input("Enter total fat grams: "))
    carb_grams = float(input("Enter total carb grams: "))
    protein_grams = float(input("Enter total protein grams: "))

    return fat_grams, carb_grams, protein_grams

def calculate_calories(f_grams, c_grams, p_grams):
    """calculate calories"""
    # initialize variables
    total_calories = 0.0
    percent_fat = 0.0
    percent_carbs = 0.0
    percent_protein = 0.0

    # process:
    # calculate total number of calories
    calories_from_fat = f_grams * 9
    calories_from_carbs = c_grams * 4
    calories_from_protein = p_grams * 4
    total_calories = (
        calories_from_fat + calories_from_carbs + calories_from_protein
    )

    # calculate percentages
    percent_fat = calories_from_fat / total_calories
    percent_carbs = calories_from_carbs / total_calories
    percent_protein = calories_from_protein / total_calories

    # print output
    print("\nOutput:")
    print("{0:8}{1:>10}{2:>13}".format("Type", "Calories", "Percentage"))

    print("{0:8}{1:10,.2f}{2:13.2%}".format("Fat", calories_from_fat, percent_fat))
    print("{0:8}{1:10,.2f}{2:13.2%}".format("Carbs", calories_from_carbs, percent_carbs))
    print("{0:8}{1:10,.2f}{2:13.2%}".format("Protein", calories_from_protein, percent_protein))