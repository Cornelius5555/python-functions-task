"""Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

Use the value from total to get the average and average to find the grade.

A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40"""
def total_marks(maths, eng, swa, sci, sos):
    totalmarks = maths + eng + swa + sci + sos
    return totalmarks

maths = int(input("Enter maths: "))
eng = int(input("Enter eng: "))
sci = int(input("Enter sci: "))
swa = int(input("Enter swa: "))
sos = int(input("Enter sos: "))
total = total_marks(maths, eng, swa, sci, sos)
print(total)

#avarage
def avarage_marks(total):
    average = total / 5
    return average
avarages = avarage_marks(total)
print(avarages)

#grade
def grade(marks):
    if avarages > 79:
        grades = "A"
    elif avarages > 60 and avarages < 79:
        grades = "B"
    elif avarages > 50 and avarages < 59:
        grades = "C"
    elif avarages > 40 and avarages < 49:
        grades = "D"
    else:
        grades = "E"
    return grades
your_grade = grade(avarages)
print(your_grade)

