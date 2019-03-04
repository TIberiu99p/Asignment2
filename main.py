def main():
    print("Select the option you wish to perform: \nA)Add student \nB)Remov student \nL)List Database \nX)Exit")
    choices = ['A','B','L','X']   
    choice = input()
    if choice == 'A':
        print("choice a works")
    elif choice == 'B':
        print("choice b works")
    elif choice == 'L':
        print("choice l works")
    elif choice == 'X':
        print("choice x works")
    else:
        if choice not in choices:
            print("Select a valid option")
            main()
            


main()
