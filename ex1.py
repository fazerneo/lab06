# I import the neccessary functions I made and stored in functions.py.
# Please view functions.py to go through the functions
from functions import Letter_Grader, Total


''' Main Program '''
# I initialize two empty lists, one to hold the student details and one to hold only student ids so that deuplicate entries are not made
student_details = []
student_Ids = []

# I use a while loop to continuously iterate until the break condition is met
while True:
    # I take student ID as input from user and turn it into an int
    Student_Id = input("Enter Student ID: ")
    Student_Id = int(Student_Id)
    
    # If the student ID is negative, zero or already exists in student_Ids list, the loop is broken
    # If the break condition is met then an error message is printed to the screen before break
    if Student_Id <= 0 or Student_Id in student_Ids:
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
    
    # We use the imported total funtion to find the total marks and store them in a variable
    # We then use the imported letter grader function to find the corresponding letter grade of the total marks
    Total_Marks = Total(Quiz1, Quiz2, Final)
    Letter_Grade = Letter_Grader(Total_Marks)
    
    # We then append the details about the student in a list form to the student_details list, which holds all student data
    student_details.append([Student_Id, Quiz1, Quiz2, Final, Total_Marks, Letter_Grade])
    
    # We print out the student data to be viewed
    print()
    print(student_details)      
    print()