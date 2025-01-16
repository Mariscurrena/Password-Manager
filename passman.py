## Password Manager
## Author: Angel Mariscurrena
## Inspo: W J Pearce

import hashlib as hash
import getpass as pwd

pwd_manager = {} ## Empty dictionary to manage all the credentials

def create_user():
    username = input("Please insert your desired username: ")
    password = input("Please insert your desired password")
    hash_pass = hash.sha256(password.encode()).hexdigest() #Recive the password, encode the password, made a hash sha256 for the password and return the value on an hexadecimal array
    pwd_manager[username] = hash_pass #Stores the hashed password with the correct user.
    print("Congrats! Your account was created successfully!!")

def login_user():
    username = input("Please enter your username: ")
    password = input("Please enter your password")
    hash_pass = hash.sha256(password.encode()).hexdigest() #Hashed the password in order to be able to compare it with the values in the dictionary and validate if the password is correct
    if username in pwd_manager.keys() and hash_pass == pwd_manager[username]:
        print(f"Welcome back {username}!! It is nice to see you again")
    else:
        print("Sorry! Your credentials are incorrect!")