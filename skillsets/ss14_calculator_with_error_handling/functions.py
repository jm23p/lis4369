"""functions py file for main"""

def get_requirements():
    """prints program requirements"""
    print("Developer: Joshua Mann")
    print("Python Calculator with Error Handling")
    print("\nProgram Requirements:\n"
        + "1. Program calculates two numbers, and rounds to two decimal places.\n"
        + "2. Prompt user for two numbers, an a suitable operator.\n"
        + "3. Use Python error handling to validate data.\n"
        + "4. Test for correct arithmetic operator.\n"
        + "5. Division by zero not permitted.\n"
        + "6. Note: Program loops until correct input entered - numbers and arithmetic operator.\n"
        + "7. Replicate display below.")

def get_valid_float(pos):
    while True:
        try:
            num = float(input("\nEnter num" + str(pos) + ": "))
            return num
            break

        except ValueError:
            print("Not valid number!")
            continue

def get_valid_operator():
    print("\nSuitable Operators: +, -, *, /, // (integer division), % (modulo operator), ** (power)")
    # operator list
    op_list = ['+', '-', '*', '/', '//', '%', '**']
    op_test = input("Enter operator: ")

    while True:
        if op_test in op_list:
            return op_test # user's input is in the list
            break

        else:
            print("Incorrect operator!")
            op_test = input("\nEnter operator: ")
            continue

def error_handling():
    """
    TypeError vs ValueError:
    Passing arguments of wrong type (e.g., passing a list when an int is expected) results in a TypeError,
    but, passing arguments with wrong value (e.g., a number outside expected boundaries) results in a ValueError.
    Below, ValueError exception testing is used below to test for *any* non-numeric value.
    And, ZeroDivisionError exception tests for division by zero.
    """

    # initialize variables
    num1 = 0.0
    num2 = 0.0
    op = ''

    # function calls
    num1 = get_valid_float(1)
    num2 = get_valid_float(2)
    op = get_valid_operator()

    # print returned values only for testing
    # print(num1)
    # print(num2)
    # print(op)

    if op == "+":
        print("{0:,.2f}".format(num1 + num2))

    elif op == "-":
        print("{0:,.2f}".format(num1 - num2))

    elif op == "*":
        print("{0:,.2f}".format(num1 * num2))

    elif op == "/":
        while True:
            try:
                print("{0:,.2f}".format(num1 / num2))
                break

            except ZeroDivisionError as err:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
                continue

    elif op == "//":
        while True:
            try:
                print("{0:,.2f}".format(num1 // num2))
                break

            except ZeroDivisionError as err:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
                continue

    elif op == "%":
        while True:
            try:
                print("{0:,.2f}".format(num1 % num2))
                break

            except ZeroDivisionError as err:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
                continue

    elif op == "**":
        print("{0:,.2f}".format(num1 ** num2))
        # or
        print("{0:,.2f}".format(pow(num1, num2)))

    else:
        print("Incorrect operator!")

    print("\nThank you for using our math calculator!")