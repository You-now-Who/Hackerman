
from time import sleep

from pwinput import pwinput

from colorama import init
from termcolor import colored

import pyfiglet


#Firebase initialisation
from unicodedata import name
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from python_files.auth import *
from python_files.game import *


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
            #print(user)
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
    return(user)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Main screen
def main_screen(user):
    while True:
        print(colored(pyfiglet.figlet_format("HackerMan"), "blue"))
        print("\nWelcome " + colored(user.child('name').get(), "green") + "!")
        print(colored("1. Tutorial", "yellow") + "\n" + colored("2. Play", "green") +  "\n" + colored("3. Leaderboard", "blue") +  "\n" + colored("4. Exit", "red"))
        choice = input("Enter your choice: ")
        if choice == "1":
            tutorial()
        elif choice == "2":
            play(user)
        
        elif choice == "3":
            leaderboard()

        elif choice == "4":
            user = None
            print("\nLogging out...")
            sleep(1)
            print("\nExiting...")
            sleep(1)
            exit()
        else:
            print("\nInvalid choice. Kindly enter again.\n")
            sleep(1)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Main function


def main():
    print("Initialising...")
    # initialise()
    os.system("cls")
    print(colored("Disclaimer: This game is made simply for fun and educational purposes. The hacking depicted in this game has been simplified and turned into something else completely. This game is to raise awarness about hacking, not to teach you how to hack. \n", "red"))
    print(colored(pyfiglet.figlet_format("HackerMan"), "blue"))
    user = start_screen()
    main_screen(user)
    

if __name__ == "__main__":
    main()