all_students = []

print('''                        
                        ######################################
                        #####   Student   Data   System  #####
                        ######################################
        ''')

def main():
    print("Select the option you wish to perform: \nA)Add student \nB)Remov student \nL)List Database \nX)Exit")
    choices = ['A','B','L','X']   
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
            print('''                        
                        ######################################
                        ####  You are exiting the program ####
                        ######################################
                ''')
            exitFuntion()
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
                print("The student {} {} already exits.".format(stud_name,stud_surname))
                is_in_List = True
       
    if is_in_List == False:
        all_students.append({
            'Name': stud_name,
            'Surname': stud_surname
        })            
                    
    with open('data.txt','w') as filehandle:
        print_once = False
        for student in all_students:
            print('\n')
            filehandle.write('%s\n' % ("Student: " + student['Name'] + ", " + student['Surname']))
            if is_in_List == False and print_once == False:
                print_once = True
                print("Student {} {} has been created".format(stud_name,stud_surname))

def RemoveStudent(all_students):
    del_stud_name = input('Enter name of the student: ')
    del_surname = input('Enter surname of the student: ')
    with open('data.txt','w') as filehandle:
        for i in range(len(all_students)):
            if all_students[i]['Name'] == del_stud_name and all_students[i]['Surname'] == del_surname:
                print("Student {} {} has been removed.".format(del_stud_name,del_surname))
                del all_students[i]
                break
                
def listStudents():
    with open('data.txt') as my_file:
        my_file.seek(0)
        first_char = my_file.read(1)
        if not first_char:
            print("List is empty,please add students.")
        else:
            my_file.seek(0)
            f = open('data.txt','r')
            if f.mode == 'r':
                contents = f.read()
                print(contents)    


def exitFuntion():
    exit()
            
main()

    
