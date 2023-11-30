"""Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd,
display  either “odd” or “even” to the user."""


def number(num):
    if num % 2 == 0:
        nums = "Even"
    else: 
        nums = "Odd"
    return nums

num = int(input("Enter your number: "))
output = number(num)
print(output)

def divisible_by_four(numss):
    if num % 4 == 0:
        Your_num = "Divisible by 4"
    else:
        Your_num = "Not divisible by 4"
    return Your_num
num = int(input("Enter your number: "))
result = divisible_by_four(num)
print(result)