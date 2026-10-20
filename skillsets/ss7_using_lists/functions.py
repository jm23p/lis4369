"""
differences between lists and arrays:
lists:
- heterogeneous (can store values of different data types)
- no need to import module/library to declare a list
- cannot perform arithmetic operations
- consumes more memory

arrays:
- homogenous (can *only* store values of same data type)
- must import module/library to declare an array
- can perform arithmetic operations
- consumes less memory
"""

def get_requirements():
    """prints program requirements"""
    print("Developer: Joshua Mann")
    print("Python Lists")
    print("\nProgram Requirements:\n"
        + "1. Lists (Python data): mutable, ordered sequence of elements.\n"
        + "2. Lists are mutable/changeable; can insert, update, delete.\n"
        + '3. Create list - using square brackets [list]: my_list = ["cherries", "apples", "bananas", "oranges"].\n'
        + "4. Create a program that mirrors the following IPO (input/process/output) format.\n"
        + "Note: User enters number of requested list elements, dynamically rendered below.\n")

def user_input():
    """function to get user input"""
    # initialize variables and list
    num = 0

    # input: get user data
    print("Input:")
    num = int(input("Enter number of list elements: "))
    return num

print() # print blank line

def using_lists(num):
    """function to get user input"""
    # process:
    my_list = [] # create empty list
    for i in range(num): # run loop num times (0 to num, exclusive)
        # prompt user for list element
        my_element = input('Please enter list element ' + str(i + 1) + ": ")
        my_list.append(my_element) # append each element to end of list

# output:
    print("\nOutput:")
    print("Print my_list:")
    print(my_list)

    elem = input("\nPlease enter list element: ")
    pos = int(input("Please enter list *index* position (note: must convert to int): "))

    print("\nInsert element into specific position in my_list: ")
    my_list.insert(pos, elem) # note: pos 1 inserts item into 2nd element
    print(my_list)

    print("\nCount number of elements in list: ")
    # also works for strings, tuples, dict objects
    print(len(my_list))

    print("\nSort elements in list alphabetically: ")
    my_list.sort() # sort alphabetically
    print(my_list)

    print("\nReverse list: ")
    my_list.reverse() # reverse list
    print(my_list)

    print("\nRemove last list element: ")
    my_list.pop() # delete last element
    print(my_list)

    print("\nDelete second element from list by *index* (note: 1 = 2nd element): ")
    # pops element at index specified
    del my_list[1]
    print(my_list)

    print("\nDelete element from list by *value* (cherries): ")
    my_list.remove('cherries')
    print(my_list)

    print("\nDelete all elements from list: ")
    my_list.clear() # deletes all elements
    print(my_list)