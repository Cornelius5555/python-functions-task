"""TASK 12: Using Python or PHP or Java or Ruby or JavaScript
Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same."""

def largest_num(num1, num2, num3, num4):
  
    if num1 != num2 !=num3 != num4:
        if num1 > num2 and num1 > num3 and num1 > num4:
            output = num1
        elif num2 > num1 and num2 > num3 and num2 > num4:
            output = num2
        elif num3 > num1 and num3 > num2 and num3 > num4:
            output = num3
        else:
            output = num4
    else:
        output = "Equall numbers entered"
    return output

num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))
num3 = int(input("Enter 3rd num: "))
num4 = int(input("Enter 4th num: "))
largest = largest_num(num1, num2, num3, num4)
print(largest)