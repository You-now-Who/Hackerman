from ast import While
from time import sleep
import os

from pwinput import pwinput

from colorama import init
from termcolor import colored

#Firebase initialisation
from unicodedata import name
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial
def tutorial():
    print("Would you like a quick tutorial? (y/n)")
    choice = input()
    if choice == "y":
        os.system('cls')
        print(colored("Great! Let's get started!", "green"))
        print("Setting up tutorial...")
        sleep(0.5)
    else:
        os.system('cls')
        print("\nStarting game...")
        sleep(1)
        return()

    print("\n Hackerman is a world full of hackers. Here, you need to be constantly on the lookout, as people  \n")

    return()