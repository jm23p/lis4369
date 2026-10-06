"""runs functions file"""
import functions as f

def main():
    """program entry"""
    f.get_requirements()
    user_input = f.get_user_input()

    # tuple unpacking: tuple values unpacked into variable names
    n1, n2, operator = user_input

    # pass user-entered values
    f.print_selection_structures(n1, n2, operator)

if __name__ =="__main__":
    main()