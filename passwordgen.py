#ask the user if want to generate password or not
#if yes, ask for password lenght
#genrate pssword
#print password
#if intial response is no ,exit program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%¨&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be"))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)


    password = "".join(password)

    print(password)

option = input("Do you want to genrate a password? (YesNo): ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program ended")
    quit()
else:
    print("Invalid input, please input Yes or No")
    quit()
