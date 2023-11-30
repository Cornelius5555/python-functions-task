"""TASK 10: Using Python or PHP or Java or Ruby or JavaScript
Write a program that calculates the total stock in a company from the array/list below if we know that the stock
is the last digit in every array/list.

prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]"""

def value_stock(stock):
    prods = [
        ["omo", "30ksh", 300],
        ["milk", "50ksh", 200],
        ["bread", "45ksh", 359],
        ["coffee", "5ksh", 79]
        ]
    stock = 0
    for i in prods:
        price = int(i[-1])
        stock += price 
        return stock
    
value = value_stock()
print(value)