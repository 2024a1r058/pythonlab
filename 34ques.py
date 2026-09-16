# WAP to take a password and check whether it contains '@' and has at least 8 characters
password = input("Enter password: ")

if '@' in password and len(password) >= 8:
    print("Valid password")
else:
    print("Invalid password")
    

