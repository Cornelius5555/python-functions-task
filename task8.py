"""TASK 8: Using Python or PHP or Java or Ruby or JavaScript
Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”.
Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points,
the function should print: “License suspended”."""
def check_limit():
    speed = int(input("Enter your Speed: "))

    speed_limit = 70
    demerit_point = 0
    if speed <= speed_limit:
        output = ("Ok")
    elif speed > speed_limit and speed < 75:
        demerit_point = 1
    else:
        demerit_point = round((speed - speed_limit) / 5)
        if demerit_point > 12:
            output = ("Licence Suspended")
        else:
            output = (demerit_point)
    return output
print(check_limit())
    