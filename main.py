#part A
all_students = []

print('''                        
                    ######################################
                    #####   Student   Data   System  #####
                    ######################################
        ''')

def main():
    print("Select the option you wish to perform: \nA)Add student \nB)Remov student \nL)List Database \nG)Add Grade \nX)Exit")
    choices = ['A','B','L','X','G']   
    choice = input("Option selected: ")

    while  True:
        if choice == 'A':
            AddStudent(all_students)
            return main()
        elif choice == 'B':
            RemoveStudent(all_students)
            return main()
        elif choice == 'L':
            listStudents()
            return main()
        elif choice == 'X':
            exitFuntion()
        elif choice == 'G':
            studGrade(all_students)
            return main()
        else:
            if choice not in choices:
                print("Select a valid option")
                return main()

def AddStudent(all_students):
    stud_name = input('Enter the name of the student: ')
    stud_surname = input('Enter the surname of the student: ')
    is_in_List = False

    if all_students != '':
         for i in range(len(all_students)):
            if all_students[i]['Name'] == stud_name and all_students[i]['Surname'] == stud_surname:
                print("\nThe student {} {} already exits.".format(stud_name,stud_surname))
                is_in_List = True
       
    if is_in_List == False:
        all_students.append({
            'Name': stud_name,
            'Surname': stud_surname,
            'Grade': 'none'
        })            
                    
    with open('data.txt','w') as filehandle:
        print_once = False
        for student in all_students:
            print('\n')
            filehandle.write('%s\n' % ("Student: " + student['Name'] + ", " + student['Surname'] + "," + "Grade: " + student['Grade']))
            if is_in_List == False and print_once == False:
                print_once = True
                print("\nStudent {} {} has been created".format(stud_name,stud_surname))
            
def RemoveStudent(all_students):
    del_stud_name = input('Enter name of the student: ')
    del_surname = input('Enter surname of the student: ')
    with open('data.txt','w') as filehandle:
        for i in range(len(all_students)):
            if all_students[i]['Name'] == del_stud_name and all_students[i]['Surname'] == del_surname:
                print("\nStudent {} {} has been removed.".format(del_stud_name,del_surname))
                del all_students[i]
                break
                
def listStudents():
    with open('data.txt') as my_file:
        my_file.seek(0)
        first_char = my_file.read(1)
        if not first_char:
            print("\nList is empty,please add students.")
        else:
            my_file.seek(0)
            f = open('data.txt','r')
            if f.mode == 'r':
                contents = f.read()
                print(contents)    


def studGrade(all_students):
    grade_name = input("Enter name of the student: ")
    grade_surname = input("Enter surname of the student: ")
    grade_letter = input("Please enter grade: A/B/C/D")
    credit = float(input("Enter credit hour: "))
    grades = ['A','B','C','D']
    validGrade = False
    while validGrade == False:
        if grade_letter == 'A':
            grade = 4.0 * credit
            validGrade = True
        elif grade_letter == 'B':
            grade = 3.0 * credit
            validGrade = True
        elif grade_letter == 'C':
            grade = 2.0 * credit
            validGrade = True
        elif grade_letter == 'D':
            gade = 1.0 * credit
            validGrade = True
        else:
            if grade_letter not in grades:
                print("Select a valid grade!")
                

            


    for i in range(len(all_students)):
        if grade_name == all_students[i]['Name'] and grade_surname == all_students[i]['Surname']:
            all_students[i]['Grade'] = str(grade)
        else:
            print ("Student doesn`t exist")
            return main()

    with open('data.txt','r+') as file1:
        for student in all_students:
            file1.write('%s\n' % ("Student: " + student['Name'] + ", " + student['Surname'] + ", " + "Grade: " + student['Grade']))
            

        
    

    
def exitFuntion():
    print('''                        
                    ######################################
                    ####  You are exiting the program ####
                    ######################################
        ''')
    exit()
            
main()

    


    
