"""functions py file for main"""

def get_requirements():
    """prints program requirements"""
    print("Developer: Joshua Mann")
    print("IT/ICT Student Percentage")
    print("\nProgram Requirements:\n"
        + "1. Find number of IT/ICT students in class."
        + "\n2. Calculate IT/ICT Student Percentage."
        + "\n3. Must use float data type (to facilitate right-alignment)."
        + "\n4. Format, right-align numbers, and round to two decimal places.")

def calculate_it_ict_student_percentage():
    """calculates percentage of students"""

    # initialize variables
    it = 0
    ict = 0
    total_students = 0
    percent_it = 0.0
    percent_ict = 0.0

    # IPO: input > process > output
    # get user data
    print("\nInput:")
    it = int(input("Enter number of IT students: "))
    ict = int(input("Enter number of ICT students: "))

    # process:
    # calculate total number of students
    total_students = it + ict

    # calculate percentage of IT students
    percent_it = it / total_students

    # calculate percentage of ICT students
    percent_ict = ict / total_students

    # print output
    print("\nOutput:")
    print("{0:17}{1:>5.2f}".format("Total Students:", total_students))
    print("{0:17}{1:>5.2%}".format("IT Students:", percent_it))
    print("{0:17}{1:>5.2%}".format("ICT Students:", percent_ict))