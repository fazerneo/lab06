''' _________Exercise 1 functions________ '''

def Total(Q1_marks, Q2_marks, Final_marks):
    
    ''' This function takes 3 parameters, Q1, Q2 and Final marks,
        A formula is applied to find the total marks,Then an if-elif-else 
        statement is used to assign letter grades according to the total marks,
        The function returns the total marks and the letter grade '''

    Total = round(float((Q1_marks * 0.20) + (Q2_marks * 0.30) + (Final_marks * 0.50)))
    
    if Total in range(80, 101):
        Letter_Grade = "HD"
    elif Total in range(70, 80):
        Letter_Grade = "D"
    elif Total in range(60, 70):
        Letter_Grade = "C"
    elif Total in range(50, 60):
        Letter_Grade = "P"
    else:
        Letter_Grade = "N"
    
    return Total, Letter_Grade    


def printDetails(studentData):

    ''' This function takes student data as its parameter, student data will be the 
    final dictionary in the main program with collected student data. This function
    will iterate through values in the main dictionary and key, values in the inner
    dictionaries. It will print key and value. The function returns the output of the
    inner code'''

    for value in studentData.values():
        for key, val in value.items():
            print(f"{key}: {val}")
        print()

    return