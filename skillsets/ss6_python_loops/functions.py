"""functions py file for main"""

def get_requirements():
    """prints program requirements"""
    print("Developer: Joshua Mann")
    print("Python Looping Structures")
    print("\nProgram Requirements:\n"
        + "1. Print while loop.\n"
        + "2. Print for loops using range() function, and implicit and explicit lists.\n"
        + "3. Use break and continue statements.\n"
        + "4. Replicate display below.\n"
        + "Note: In Python, for loop used for iterating over a sequence (i.e., list, tuple, dictionary, set, or string).\n")

def print_loops():
    """displays various looping structures and range() function"""
    # loop structures

    print("1. while loop:")
    i = 1
    while i <= 3:
        print(i)
        i = i + 1

    print("\n2. for loop: using range() function with 1 arg:")
    # prints 0-3, not including 3
    for i in range(4):
        print(i)

    print("\n3. for loop: using range() function with 2 args:")
    # calling with 2 args creates sequence of numbers from 1st to 2nd, not including 2nd
    for i in range(1, 4):
        print(i)

    print("\n4. for loop: using range() function with 3 args (interval 2):")
    # 3rd argument is interval
    # [1, 3]
    for i in range(1, 4, 2):
        print(i)

    print("\n5. for loop: using range() function with 3 args (negative interval):")
    # interval can be negative
    # [3, 1]
    for i in range(3, 0, -2):
        print(i)

    print("\n6. for loop using (implicit) list (i.e., list not assigned to variable):")
    # prints 1 - 3, including 1 and 3
    for i in [1, 2, 3]:
        print(i)

    print("\n7. for loop iterating through (explicit) string list:")
    states = ['Michigan', 'Alabama', 'Florida']
    for state in states:
        print(state)

    print("\n8. for loop using break statement (stops loop):")
    # break statement stops loop
    states = ['Michigan', 'Alabama', 'Florida']
    for state in states:
        if state == "Alabama":
            break
        print(state)

    print("\n9. for loop using continue statement (stops and continues with next):")
    # continue statements stops current iteration, and continues with next
    states = ['Michigan', 'Alabama', 'Florida']
    for state in states:
        if state == "Alabama":
            continue
        print(state)

    print("\n10. print list length:")
    states = ['Michigan', 'Alabama', 'Florida']
    print(len(states))