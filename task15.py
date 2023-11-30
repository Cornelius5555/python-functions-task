"""TASK 15: Using Python or PHP or Java or Ruby or JavaScript
Write a program that takes input of someone's basic salary and benefits,
adds them to find the gross salary then uses  the gross salary to find the NHIF. """


def calc_gross(basic_salary, benefits):
    gros_sall = basic_salary + benefits
    return gros_sall

basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits: "))
gros_salary = calc_gross(basic_salary, benefits)
print(f" gross salary: {gros_salary}")

#nhif
def calc_hnif(gros_salary):
    nhif = ""
    if gros_salary < 6000:
        nhif = 150
    elif gros_salary > 6000 and gros_salary < 7999:
        nhif = 300
    elif gros_salary > 7999 and gros_salary < 11999:
        nhif = 400
    elif gros_salary > 11999 and gros_salary < 14999:
        nhif = 500
    elif gros_salary > 14999 and gros_salary < 19999:
        nhif = 600
    elif gros_salary > 19999 and gros_salary < 24999:
        nhif = 750
    elif gros_salary > 24999 and gros_salary < 29999:
        nhif = 850
    elif gros_salary > 29999 and gros_salary < 34999:
        nhif = 900
    elif gros_salary > 34999 and gros_salary < 39999:
        nhif = 950
    elif gros_salary > 39999 and gros_salary < 44999:
        nhif = 1000
    elif gros_salary > 44999 and gros_salary < 49999:
        nhif = 1100
    elif gros_salary > 49999 and gros_salary < 59999:
        nhif = 1200
    elif gros_salary > 59999 and gros_salary < 69999:
        nhif = 1300
    elif gros_salary > 69999 and gros_salary < 79999:
        nhif = 1400
    elif gros_salary > 79999 and gros_salary < 89999:
        nhif = 1500
    elif gros_salary > 89999 and gros_salary < 99999:
        nhif = 1600
    else:
        nhif = 1700
    return nhif
NHIF = calc_hnif(gros_salary)
print(f"nhif: {NHIF}")

#nssf
def calc_nssf(gros_salary):
    nssf = ""
    if gros_salary > 0 and gros_salary <= 18000:
        nssf = gros_salary * 0.06
    else:
        nssf = 18000 * 0.06
    return nssf
NSSF = calc_nssf(gros_salary)
print(f"nssf: {NSSF}")

#nhdf
def calc_nhdf(gros_salary):
    nhdf = gros_salary * 0.015
    return nhdf
Nhdf = calc_nhdf(gros_salary)
NHDF = round(Nhdf, 2)
print(f"nhdf: {NHDF}")

#taxable income
def calc_taxableincome(gros_salary, NSSF, NHDF):
    taxableincome = gros_salary - (NSSF + NHDF)
    return taxableincome

taxable_income = calc_taxableincome(gros_salary, NSSF, NHDF)
print(f"taxable income: {taxable_income}")


#payee
def calc_payee(taxable_income):
    payee = ""
    if taxable_income <= 24000:
        payee = taxable_income * 0.1
    elif taxable_income > 24000 and taxable_income < 32333:
        payee = ((taxable_income - 24000) * 0.25) + (24000 * 0.1) - 2400
    elif taxable_income > 32333 and taxable_income < 500000:
        payee = ((taxable_income - 32333) * 0.3) + (24000 * 0.1) + (8333 * 0.25)- 2400
    elif taxable_income > 50000 and taxable_income < 800000:
        payee = ((taxable_income - 500000) * 0.325) + (24000 * 0.1) + (8333 * 0.25) + (467667 *0.3) - 2400
    else:
        payee = ((taxable_income - 800000) * 0.35) + (24000 * 0.1) + (8333 * 0.25) + (467667 * 0.3) + (300000 * 0.325) - 2400
    return payee

payee = calc_payee(taxable_income)
Payee = round(payee, 2)
print(f"payee: {Payee}")

#net salary
def calc_net_salary(gros_salary, NHIF, NHDF, NSSF, Payee):
    net_salary = gros_salary - (NHIF + NHDF +  NSSF + Payee)
    return net_salary

net_salary = calc_net_salary(gros_salary, NHIF, NHDF, NSSF, Payee)
print(f"net salary: {net_salary}")
