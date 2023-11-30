from datetime import date

def calculate_age(birth_date, current_date):
    # Calculate years, months, and days
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    # Adjust for negative differences
    if days < 0:
        months -= 1
        days += get_days_in_month(birth_date.month, birth_date.year)
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def get_days_in_month(month, year):
    # Returns the number of days in a given month and year
    if month == 2:  # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29  # Leap year
        else:
            return 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:
        return 31

# User input for date of birth
birth_day = int(input("Enter your birth day: "))
birth_month = int(input("Enter your birth month: "))
birth_year = int(input("Enter your birth year: "))

# Current date
current_date = date.today()

# Create date object for birth date
birth_date = date(birth_year, birth_month, birth_day)

# Check if the birth date is valid
if birth_date <= current_date:
    # Calculate age
    age_years, age_months, age_days = calculate_age(birth_date, current_date)
    print(f"Your age is {age_years} years, {age_months} months, and {age_days} days.")
else:
    print("Please enter a valid date of birth.")
