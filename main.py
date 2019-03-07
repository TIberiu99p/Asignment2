all_students = []

def main():
    print("Select the option you wish to perform: \nA)Add student \nB)Remov student \nL)List Database \nX)Exit")
    choices = ['A','B','L','X']   
    choice = input()
    running = False
    while running == False:
        second_choice = input()
        if choice == 'A':
            AddStudent(all_students)
            print("Press R for return >: ")
            if second_choice == 'R':
                main()
        elif choice == 'B':
            print("choice b works")
            main()
            break
        elif choice == 'L':
            print("choice l works")
            main()
            break
        elif choice == 'X':
            running = True
        else:
            if choice not in choices:
                print("Select a valid option")
                main()

def AddStudent(all_students):
    stud_name = input('Enter the name of the student: ')
    stud_surname = input('Enter the surname of the student: ')
    all_students.append({
        'Name': stud_name,
        'Surname': stud_surname
    })
    for student in all_students:
        print('\n')
        for key, value in student.items():
            print ('{0}: {1}'.format(key,value))
            

main()
