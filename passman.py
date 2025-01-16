## Password Manager
## Author: Angel Mariscurrena
## Inspo: W J Pearce

import hashlib as hash
import getpass as pwd
import time
import os

pwd_manager = {} ## Empty dictionary to manage all the credentials

def wait(duration):
    time.sleep(duration)
    os.system('clear')
    
def create_user():
    username = input("Please provide your desired username: ")
    #password = input("Please provide your desired password: ")
    password = pwd.getpass("Please provide your desired password: ")
    password_validation = pwd.getpass("Please provide your desired password again: ")
    if password == password_validation:
        hash_pass = hash.sha256(password.encode()).hexdigest() #Recive the password, encode the password, made a hash sha256 for the password and return the value on an hexadecimal array
        pwd_manager[username] = hash_pass #Stores the hashed password with the correct user.
        print("Congrats! Your account was created successfully!!")
    else:
        print("Sorry! Your password doesn't match :c\n Try again!")
        

def login_user():
    username = input("Please enter your username: ")
    password = pwd.getpass("Please enter your password: ")
    hash_pass = hash.sha256(password.encode()).hexdigest() #Hashed the password in order to be able to compare it with the values in the dictionary and validate if the password is correct
    if username in pwd_manager.keys() and hash_pass == pwd_manager[username]:
        print(f"\nWelcome back {username}!! It is nice to see you again c:")
        opt = input(f"\nWhat do you want to do {username}\n 1. Continue exploring\n 2. Logout\n")
        if opt == '2':
            print(f"\nSee you soon, {username} c:")
            wait(1)
            exit()
    else:
        print("Sorry! Your credentials are incorrect! \n Try again c:")
        wait(1)

def main():
    os.system('clear')
    print("Welcome to the password manager program!!")
    while True: #Allows to use multiple times the program and store into the dictonary the credentials
        print("\nPlease select one of the following options: \n 1. Create an Account \n 2. Login into your account \n 3. Exit")
        opt = input("Option: ")
        if opt == "1":
            print("\nYou selected the create account feature!\n")
            create_user()
        elif opt == "2":
            print("\nYou selected the login account feature!\n")
            login_user()
        elif opt == "3":
            print("\nBye c:")
            wait(1)
            exit()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()