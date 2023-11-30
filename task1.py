#Write a program that prompts the user to enter the base and height of a triangle and returns its area.


def area_tringle(base, height):
    area = (base * height) / 2
    return area

base = int(input("Enter base: "))
height = int(input("Enter height: "))
areaa = area_tringle(base, height)
print(areaa)