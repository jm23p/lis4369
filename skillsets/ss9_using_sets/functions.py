"""function module for SS8"""


def get_requirements():
    """prints program requirements"""
    print("Developer: Joshua Mann")
    print("Python Sets")
    print("\nProgram Requirements:\n"
        + "1. Sets (Python data structure): mutable, heterogeneous, unordered sequence of elements, *but* cannot hold duplicate values.\n"
        + "2. Sets are mutable/changeable; can be inserted, updated, or deleted.\n"
        + "3. While sets are mutable/changeable, they *cannot* contain other mutable items like list, set, or dictionary:\n\t the elements in the set must be immutable.\n"
        + "4. Since sets are unordered, cannot use indexing (or slicing) to access, update, or delete elements.\n"
        + "5. Note: An \"iterable\" is *any* object, whicih can be iterated over; lists, tuples, or strings.\n"
        + "6. Create a program that mirrors the following IPO (input/process/output) format.\n")

def using_sets():
    """function displays set output""" 
    # input: 
    print("Input: Hard coded - no user input. See thre examples above.")
    print("***Note***: All three sets below print as \"sets\" (i.e., curly brackets), *regardless* of how they were created!\n")

    # initialize variables and set
    my_set = {1, 3.14, 2.0, 'four', 'Five'} # create set
    print("Print my_set created using curly brackets:")
    print(my_set)
    # note: each run displays strings 

    print("\nPrint type of my_set:")
    print(type(my_set))
    # note: because sets are unordered, {1, 2} and {2, 1} are the same set

    my_set1 = set([1, 3.14, 2.0, 'four', 'Five'])
    print("\nPrint my_set1 created using set() function with list:")
    print(my_set1)

    print("\nPrint type of my_set1:")
    print(type(my_set1))

    my_set2 = set((1, 3.14, 2.0, 'four', 'Five'))
    print("\nPrint my_set2 created using set() function with tuple:")
    print(my_set2)

    print("\nPrint type of my_set2:")
    print(type(my_set2))

    print("\nLength of my_set:")
    print(len(my_set))

    print("\nDiscard 'four':")
    my_set.discard('four')
    print(my_set)

    print("\nRemove 'Five':")
    my_set.remove('Five')
    print(my_set)
    # when attempting to delete an item that doesnt exist in setm discard() ignores it, but remove() raises a KeyError

    print("\nLength of my_set:")
    print(len(my_set))

    print("\nAdd element to set (4) using add() method:")
    my_set.add(4)
    print(my_set)

    print("\nLength of my_set:")
    print(len(my_set))

    print("\nDisplay minimum number:")
    print(min(my_set))

    print("\nDisplay maximum number:")
    print(max(my_set))

    print("\nDisplay sum of numbers:")
    print(sum(my_set))

    print("\nDelete all set elements:")
    my_set.clear()
    print(my_set)

    print("\nLength of my_set:")
    print(len(my_set))