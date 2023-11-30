def calc_gross(basic_salary, benefits):
    gross_salary = basic_salary + benefits
    return gross_salary 

basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits: "))
grossalary = calc_gross(basic_salary, benefits)
print(grossalary)