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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial
def tutorial():
    print("Would you like a quick tutorial? (y/n)")
    choice = input()
    if choice == "y":
        print(colored("Great! Let's get started!", "green"))
    else:
        print("\nStarting game...")
        sleep(1)
        return()
