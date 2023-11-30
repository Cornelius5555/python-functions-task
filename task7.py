"""TASK 7: Using Python or PHP or Java or Ruby or JavaScript
Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40"""

def your_grade():
    marks = range(0, 101)
    grade =int(input("Enter your Grade: "))
    if grade in marks:
        if grade > 79:
            output = "A"
        elif grade > 60 and grade < 79:
            output = "B"
        elif grade > 59 and grade < 49:
            output = "C"
        elif grade > 49 and grade < 40:
            output = "D"
        else:
            output = "E"
    else:
        output = ("Invalid grade entered")
    return output
print(your_grade())