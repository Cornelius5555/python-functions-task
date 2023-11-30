"""TASK 9: Using Python or PHP or Java or Ruby or JavaScript
Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
Example If rows is 5, it should print the following:
*
**
***
****
*****....."""

def print_stars(rows):
    for i in range(1, rows + 1):
        print("*" * i)

# Get input from the user
try:
    num_rows = int(input("Enter the number of rows: "))
    if num_rows <= 0:
        print("Please enter a positive integer.")
    else:
        print_stars(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
