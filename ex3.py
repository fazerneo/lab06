from functions import main_menu

student_data = {}
deans_list = []
IDs = []

while True:
    
    user_input = main_menu()
    user_input = int(user_input)
    
    ''' Entering Student Data '''

    if user_input == 1:
        print()
        student_ID = input("Please enter Student ID number: ")
        student_ID = int(student_ID)

        if student_ID not in range(1000, 2001) or student_ID in IDs:
            print("\nError: Invalid Student ID")
            break

        IDs.append(student_ID)
 
        student_name = input("Please enter Student name: ")
    
        while True:
            GPA = float(input("Please enter student GPA between 0-4: "))
            if GPA > 0 and GPA < 4:
                break
        major = input("Please enter the major of the student: ")
        contact = input("Please enter the contact number: ")
        
        student_data[student_ID] = {
            "student_ID": student_ID, 
            "student_name": student_name, 
            "GPA": GPA, 
            "major": major, 
            "contact number": contact
        }
        
        print()
        print('Data Add Successful')
        print() 
    
    ''' Searching for a student using their name '''

    if user_input == 2:
        search = input("Please enter the name of the student you want to search for: ")
        for i in student_data.values():
            if i['student_name'] == search:
                print()
                print(f"The student data is as below: \n{i}")
        print()        

    ''' Deleting a Student's record '''

    if user_input == 3:
        delete = input("Please enter the name of the student whose details you want to delete: ")
        for key, value in student_data.copy().items():
            if value.get('student_name') == delete:
                del student_data[key]

        print()
        print('Data Delete Successful')
        print()
            
    ''' Viewing the Dean's List '''

    if user_input == 4:
        for i in student_data.values():
            if i['GPA'] >= 3.75:
                print()
                deans_list.append(i['student_name'])
                print(f"the students in the dean's list are \n{deans_list}")
                print()

    ''' Viewing all data '''

    if user_input == 5:
        num = 0
        print()
        for i in student_data.values():
            num +=1
            print(f"Data entry {num} \n{i}")
            print()


    ''' Exit Program '''

    if user_input == 6:
        print()
        print("Thank you for visiting")
        print()
        break
        