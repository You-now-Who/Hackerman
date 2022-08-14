from time import sleep

from pwinput import pwinput

from colorama import init
from termcolor import colored

#Firebase initialisation
from unicodedata import name
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from python_files.tutorial import tutorial


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Login function
def login(dbref):
    print("\nGetting login details...")
    sleep(0.2)

    user = None

    while True:

        print("Enter " + colored("Username: ", "green"))
        username = input()
    
        print("Enter " + colored("Password: ", "green"))
        password = pwinput()

        if dbref.child('users').child(username).get() == None:
            print(colored("Username does not exist", "red") + "\n Do you want to register? (y/n)")
            choice = input()
            if choice == "y":
                user = register(dbref)
                return(user)

        elif dbref.child('users').child(username).child('password').get() == password:
            user = dbref.child('users').child(username)
            print(colored("\nLogin successful.\n", "green"))
            break

        else:
            print(colored("Passwords do not match", "red") + "\n Do you want to register? (y/n)")
            choice = input()
            if choice == "y":
                user = register(dbref)
                return(user)

        print("\nRetrying login....\n")


    tutorial()

    return(user)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Register function
def register(dbref):
    print("\nRegistering...")
    
    #Get username
    username = ''
    while True:
        print("Enter " + colored("Username: ", "green"))
        username = input()
        if username == "":
            print(colored("Username cannot be empty", "red"))
        elif dbref.child('users').child(username).get() != None:
            print(colored("Username already exists", "red"))
        else:
            break
    
    #Get password
    password = ''
    while True:
        print("Enter " + colored("Password: ", "green"))
        password = pwinput()
        if password == "":
            print(colored("Password cannot be empty \n", "red"))
        else:
            break    
    
    #Get name
    name = ''
    while True:
        print("Enter " + colored("Name: ", "green"))
        name = input()
        if name == "":
            print(colored("Name cannot be empty", "red"))
        else:
            break

    print("\nRegistering user...")

    #Add user to database
    dbref.child('users').child(username).set({
        'password': password,
        'name': name,
        'points': 0
    })
    user = dbref.child('users').child(username)
    print(colored("\nRegistration successful.\n", "green"))
    print(colored("Login successful.\n", "green"))
    
    #Start the tutorial
    tutorial()

    return(user)