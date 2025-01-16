## Password Manager
## Author: Angel Mariscurrena
## Inspo: W J Pearce

import hashlib as hash
import getpass as pwd
import time
import os

pwd_manager = {} ## Empty dictionary to manage all the credentials

def create_user():
    username = input("Please provide your desired username: ")
    password = input("Please provide your desired password: ")
    hash_pass = hash.sha256(password.encode()).hexdigest() #Recive the password, encode the password, made a hash sha256 for the password and return the value on an hexadecimal array
    pwd_manager[username] = hash_pass #Stores the hashed password with the correct user.
    print("Congrats! Your account was created successfully!!")

def login_user():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    hash_pass = hash.sha256(password.encode()).hexdigest() #Hashed the password in order to be able to compare it with the values in the dictionary and validate if the password is correct
    if username in pwd_manager.keys() and hash_pass == pwd_manager[username]:
        print(f"Welcome back {username}!! It is nice to see you again c:")
    else:
        print("Sorry! Your credentials are incorrect!")

def main():
    os.system('clear')
    print("Welcome to the password manager program!!")
    while True: #Allows to use multiple times the program and store into the dictonary the credentials
        print("\nPlease select one of the following options: \n 1. Create an Account \n 2. Login into your account \n 3. Exit")
        opt = input("Option: ")
        if opt == "1":
            print("You selected the create account feature!")
            create_user()
        elif opt == "2":
            print("You selected the login account feature!")
            login_user()
        elif opt == "3":
            print("Bye c:")
            time.sleep(2)
            exit()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()