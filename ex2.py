# I import the neccessary functions I made and stored in functions.py.
# Please view functions.py to go through the functions
from functions import Total, printDetails, AHL, topper_lowest, failure


''' __________Main Program_________ '''

# I initialize two empty lists, one to hold the student details and one to hold only student ids
# so that deuplicate entries are not made
student_details = {}
student_Ids = []

# I use a while loop to continuously iterate until the break condition is met
while True:
    
    Student_name = input("Enter Student name: ")
    
    # I take student ID as input from user and turn it into an int
    Student_Id = input("Enter Student ID (Between 1000 & 2000): ")
    Student_Id = int(Student_Id)
    
    # If the student ID is not in the range 1000 and 2000 or student id duplicated, the loop is broken
    # If the break condition is met then an error message is printed to the screen before break
    if Student_Id not in range(1000, 2001) or Student_Id in student_Ids:
        print("\nError: Invalid Student ID")
        break
    
    # If the break condition is not met, the student_id is appended to the student_ids list
    student_Ids.append(Student_Id)
    
    # we then take inputs for Quiz1, Quiz2 and Final marks
    # We turn the marks into int and validate whether they are in between zero and 100.
    # If the marks are not valid, the user is continuously asked for valid marks
    # If valid marks is entered, we move on to the next step
    Quiz1 = input("Enter Q1: ")
    Quiz1 = int(Quiz1)
    while Quiz1 not in range(0, 101):
        Quiz1 = input("Please enter valid marks between 0 and 100: ")
        Quiz1 = int(Quiz1)
        if Quiz1 in range(0, 101):
            break
        
    Quiz2 = input("Enter Q2: ")
    Quiz2 = int(Quiz2)
    while Quiz2 not in range(0, 101):
        Quiz2 = input("Please enter valid marks between 0 and 100: ")
        Quiz2 = int(Quiz2)
        if Quiz2 in range(0, 101):
            break
        
    Final = input("Enter Final: ")
    Final = int(Final)
    while Final not in range(0, 101):
        Final = input("Please enter valid marks between 0 and 100: ")
        Final = int(Final)
        if Final in range(0, 101):
            break
    
    # We use the imported total funtion to find the total marks and letter grade and store them in variables
    (Total_Marks, Letter_Grade) = Total(Quiz1, Quiz2, Final)
    
    
    # We then append the details about the student in a dictionary form to the student_details list, 
    # which holds all student data. The key we use for each chunk of data (in dictionary form) is student ID.
    student_details[Student_Id] = {
        "Name" : Student_name,
        "StudentID": Student_Id,
        "Q1" : Quiz1,
        "Q2:" : Quiz2,
        "Final" : Final, 
        "UnitMark" : Total_Marks, 
        "Grade" : Letter_Grade
    }
    
    # We print out the student data to be viewed by calling the imported printDetails function with 
    # student_details dictionary as parameter
    print()
    printDetails(student_details)
    
    # Use the imported AHL function and print out average, highest marks and lowest marks
    (Average, Highest_marks, Lowest_marks) = AHL(student_details)
    print(f"Average Marks in unit is: {Average}")
    print(f"Highest Marks in unit is: {Highest_marks}")
    print(f"Lowest Marks in unit is: {Lowest_marks}" )
    print()
    
    (topper_name, topper_ID, lowest_name, lowest_ID) = topper_lowest(student_details)
    print(f"the highest scorer of the unit is {topper_name} with Student_ID number {topper_ID}")
    print(f"the lowest scorer of the unit is {lowest_name} with Student_ID number {lowest_ID}")
    print()

    print(f"{failure(student_details)} failed the unit")
