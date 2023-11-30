"""TASK 5: Using Python or PHP or Java or Ruby or JavaScript
Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
The goal of this exercise is to think about some internals that programs normally take care of for us. """


def check_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        output = f"1st number is the largest: {num1}"
    elif num2 > num1 and num2 > num3:
        output = f"2nd number is the largest: {num2}"
    else:
        output = f"3rd number is the largest: {num3}"
    return output

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
number = check_number(num1, num2, num3)
print(number)