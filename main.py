from ast import While
from time import sleep

from pwinput import pwinput

from colorama import init
from termcolor import colored

#Firebase initialisation
from unicodedata import name
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from python_files.auth import *

#Global variables
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://minecare-2e2c7-default-rtdb.firebaseio.com"})

dbref = db.reference('/')

user = None


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Initialise Firebase
def initialise():
    try:
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {'databaseURL': "https://minecare-2e2c7-default-rtdb.firebaseio.com"})

        dbref = db.reference('/')
        users = dbref.child('users')
        print("Initialisation successful. \n")
        return
    except:
        print("Initialisation failed, exiting...")
        sleep(1)
        exit()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Start screen
def start_screen():
    while True:
        print("Hello, and welcome to the world of HackerMan! \n Would you like to login or register?")
        print(colored("1. Login", 'green') + "\n" + colored("2. Register", 'yellow') + "\n" + colored("3. Exit", 'red'))
        choice = input("Enter your choice: ")
        if choice == "1":
            user = login(dbref)
            print(user)
            if user != None:
                break
        elif choice == "2":
            user = register(dbref)
            if user != None:
                break
        elif choice == "3":
            print("\n Exiting...")
            exit()
        else:
            print("\nInvalid choice. Kindly enter again.\n")
            sleep(1)


def main():
    print("Initialising...")
    # initialise()
    start_screen()
    

if __name__ == "__main__":
    main()