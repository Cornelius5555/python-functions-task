"""TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123”
, if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you
have been blocked"""

def check_username(email, passsword):
   
    attempts = 3  
    for i in range(attempts):
        email = "admin@gmail.com"
        passsword = "admin@123" 
        
        if your_email == email and your_pass == passsword:
            output = "Access the granted"
            break
        else:
            attempts += 1
            if attempts > 3:
                output = "Invalid username or password"
                attempts-i-1
            else:
                output = "account locked"
    return output
            
your_email = input("Enter your email: ")
your_pass = input("Enter your pass: ")  
logins = check_username(your_email, your_pass)
print(logins)
