valid_password = False
number_attempts = 0


print ("Please type in your password to enter the secret gateway..."
        "\n - Password is atleast 6 characters long"
        "\n - has atleast one capital letter"
        "\n - has atleast one symbol")

password_entered = input ("Please enter your password: ")

while not valid_password:
    number_attempts = number_attempts + 1.3

    if len(password_entered) < 6:
           print("\n password must be atleast 6 characters long")
    elif password_entered.isalpha():
            print("\n password must have atleast one symbol")
    elif password_entered.islower():
            print("\n password must have atleast one capital letter")
    else:
            valid_password = True
            continue
    if number_attempts > 3 and number_attempts < 4:
        print ("Careful... you have one more try")
    elif number_attempts > 4:
        print("\n Too many attempts, we are altering the authorities")
        break 
    password_entered = input("Please enter another password: ")
                            
else:
    print("You may enter the club")
