import time
import random
from termcolor import colored

#Firebase initialisation
from unicodedata import name
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from python_files.typing import words, typing_game
from python_files.hangman import hangman, init_hangman, memory, scramble


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def start_game(user, mode):
    player_is = "neutral"
    if mode == "1":
        if random.randint(1,2) == 1:
            player_is = "hacker"
        else:
            player_is = "security"

    if player_is == "hacker":
        print(colored("You are the hacker", "red"))
        print("Objective: Hack one of the network ports with any method")

        ports = []
        for i in range(4):
            ports.append(random.randint(1000,9999))

        available_commands = []

        while True:
                command = input("Enter your command: ")
                


    elif mode == "2":
        print("This feature is not yet available")

    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def play_screen():
    while True:

        print("\nWhat would you like to do?")
        print(colored("1. Play Offline", 'green') + "\n" + colored("2. Play Online", 'blue') + "\n" + colored("3. Exit", 'red'))
        choice = input("Enter your choice: ")
        if choice == "1":
            return("offline")
        elif choice == "2":
            print("This feature is not yet available")
            continue
        else:
            print(colored("Invalid choice", "red"))
            continue



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def play(user):

    mode = play_screen()
    start_game(user, mode)
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    