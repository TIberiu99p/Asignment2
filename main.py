all_students = []

def main():
    print("Select the option you wish to perform: \nA)Add student \nB)Remov student \nL)List Database \nX)Exit")
    choices = ['A','B','L','X']   
    choice = input()
    
    
    while True:
        if choice == 'A':
            AddStudent(all_students)
            return main()
        elif choice == 'B':
            RemoveStudent(all_students)
            return main()
        elif choice == 'L':
            print("choice l works")
        elif choice == 'X':
            break
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
    with open('data.txt','w') as filehandle:
        for student in all_students:
            print('\n')
            filehandle.write('%s\n' % student)
            for key, value in student.items():
                print (str('{0}: {1}'.format(key,value)))
            
def RemoveStudent(all_students):
    del_stud_name = input('Enter name of the student: ')
    del_surname = input('Enter surname of the student: ')
    for i in range(len(all_students)):
        if all_students[i]['Name'] == del_stud_name and all_students[i]['Surname'] == del_surname:
            del all_students[i]
            break
    
    
        

        
            
main()
