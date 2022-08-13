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
#Hack tutorial
def hack():
    print("\n Hack is the process of taking data from a system and modifying it. \n")
    sleep(0.4)
    print("A hacker needs to find " + colored("vulnerabilities", "red") + " in a system to hack it. There are many fields in hacking, but today, we are going to focus on hacking other " + colored("networks", "blue") + ". \n")
    sleep(1)

    print("Each computer")

    return()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Secure tutorial
def secure():
    print("\n Secure is the process of securing a system. \n")
    sleep(0.4)
    print("\n You can secure a system by: \n" + colored("1. Searching for a vulnerability", "red") + " \n" + colored("2. Finding a vulnerability", "green"))
    return()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Main Tutorial
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

    print("\n Hackerman is a world full of hackers and cyberpolice, at war with each other. Here, you can play both as a " + colored("Hacker", "red") + " or a " + colored("Cybersecurity Official", "green") +  "\n")
    sleep(0.4)
    print("\n What do you want to learn about first? \n" + colored("1. Hack", "red") + " \n" + colored("2. Secure", "green"))

    choice = input()

    if choice == "1":
        hack()
    elif choice == "2":
        secure()

    return()


tutorial()