def validate_password():
    correct_password = "admin@123"
    attempts = 4

    while attempts > 0:
        user_input = input("Enter the password: ")

        if user_input == correct_password:
            output = ("Access granted! Welcome.")
            break
        else:
            attempts -= 1
            output = (f"Incorrect password. {attempts} attempts remaining.")

    if attempts == 0:
        output = ("Account blocked. Please contact support for assistance.")
    return output

# Call the function to start password validation
print(validate_password())
