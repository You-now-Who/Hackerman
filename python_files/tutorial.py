from ast import While
from multiprocessing import current_process
from time import sleep
import time
import random
import os

from pwinput import pwinput

from colorama import init
from termcolor import colored

#Firebase initialisation
# from unicodedata import name
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

from python_files.typing import words, typing_game
from python_files.hangman import hangman, init_hangman



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Hack tutorial
def hack():
    current_port = 0
    print("\nHack is the process of taking data from a system and modifying it. \n")
    sleep(0.4)
    print("A hacker needs to find " + colored("vulnerabilities", "red") + " in a system to hack it. There are many fields in hacking, but today, we are going to focus on hacking other " + colored("networks", "blue") + ". \n")
    sleep(1)

    print("In this game, there are various network " + colored("ports", "blue") + " \n")
    sleep(0.4)
    ports = [4020, 8000, 1900, 6000]

    print("\nYou need to scan the ports using the " + colored("scan", "red") + " command.")

    while True:
        command = input("Scan for the ports by using the " + colored("scan", "red") + " command: ")
        if command == "scan":
            print("\nScanning ports...")
            sleep(2)
            print("\nAll ports have been scanned")
            break
        else:
            print("\nWrong command")
            continue

    for port in ports:
        print(colored(port, "blue"), end="")
        print("    ", end="")
    
    print("\n")
    sleep(0.4)
    print("You can enter these ports by using the " + colored("cd", "red") + " command. Try using "  + colored("cd", "red") + " " + colored("4020", "blue") + " to enter port 4020" + " \n")
    sleep(0.4)
    while True:
        command = input("Use the cd command on port " + colored("4020", "blue") + ": ")
        if command == "cd 4020":
            current_port = 4020
            print("\nYou have entered port " + colored(current_port, "blue") + " \n")
            break
        else:
            print("\nWrong command")
            continue
    
    print("Now, you can initiate an attack on the port " + colored(current_port, "blue") + ". There are 3 types of attacks: \n")
    sleep(0.4)
    
    not_learnt = [{"DoS": "blue"}, {"MITM": "green"}, {"Spoofing": "red"}]

    while True:        
        
        print("\n1. " + colored("DoS", "blue") + " \n2. " + colored("MITM", "green") + " \n3. " + colored("Spoofing", "red") + " \n")

        sleep(0.2)
        print("How do you want to continue?")
        
        while True:
            command = input()
            if command == "1":
                print("\nYou have chosen " + colored("DoS", "blue") + ". Excellent choice! A DoS, or Denial of Service attack is a type of attack where a hacker sends a " + colored("large amount of data", "green") + " to a target, usually to overwhelm the resources of a system \n")
                print("You can initiate a DoS attack on the port " + colored(current_port, "blue") + " by using the " + colored("dos", "red") + " command. \n")

                while True:
                    command = input("Initiate a DoS attack on port " + colored(current_port, "blue") + ": ")
                    if command == "dos":
                        print("\nInitiating DoS attack on port " + colored(current_port, "blue") + "...")
                        sleep(2)
                        print("\nDoS attack on port " + colored(current_port, "blue") + " has been initiated")
                        break
                    else:
                        print("\nWrong command")
                        continue

                print("\n \n Now comes the " + colored("fun part", "green")+ "! You need to function quickly and effectively in the coming seconds for a successful attack. You need to type and enter the " + colored("words", "red") + " that appear on your screen in quick succession to send them to the other system's computer\n")
                sleep(0.4)
                print("You need to type the words quickly, before the victim is alerted to the presence of a hacker. \n")

                points = typing_game()

                if points >= 0:
                    print("\nYou have " + colored("successfully", "green") + " hacked the system! \n")
                    print("\nYou have gained " + colored(points, "green") + " points! \n")
                else:
                    print(colored("\nYour attack was too slow, and the people were alerted \n", "red"))

                try:
                    for i in not_learnt:
                        if list(i.keys())[0] == "DoS":
                            not_learnt.remove(i)
                except KeyError:
                    pass

                print("\nWhat would you further want to know about?\n")
                sleep(1)

                break

            elif command == "2":
                print("\nYou have chosen " + colored("MITM", "green") + ". Excellent choice. A MITM attack is a type of attack where a hacker " +  colored("intercepts", "blue") + " the data that is sent between two systems and modifies it.")
                
                print("\nYou can initiate a MITM attack on the port " + colored(current_port, "blue") + " by using the " + colored("mitm", "red") + " command. \n")
                while True:
                    command = input("Initiate a MITM attack on port " + colored(current_port, "blue") + ": ")
                    if command == "mitm":
                        print("\nInitiating MITM attack on port " + colored(current_port, "blue") + "...")
                        sleep(2)
                        print("\nMITM attack on port " + colored(current_port, "blue") + " has been initiated")
                        break
                    else:
                        print("\nWrong command")
                        continue
                
                print("You now have to listen to do the port, for any information that is sent. \n")
                print("You can listen to the port by using the " + colored("listen", "red") + " command. \n")
                while True:
                    command = input("Listen to the port " + colored(current_port, "blue") + ": ")
                    if command == "listen":
                        print("\nListening to port " + colored(current_port, "blue") + "...")
                        sleep(random.randint(3,5))
                        print("\nYou have listened to the port " + colored(current_port, "blue") + " and you could only find an encoded message. You need to decode that message: ")
                        sleep(0.4)

                        init_hangman(words())
                        result = hangman()

                        if result == True:
                            print("\nYou have successfully decoded the message! \n")
                            points = (random.randint(5,30))
                            print("\nYou have gained " + colored(points, "green") + " points! \n")
                        else:
                            print("\nYou have failed to decode the message! \n")

                        try:
                            for i in not_learnt:
                                if list(i.keys())[0] == "MITM":
                                    not_learnt.remove(i)
                        except KeyError:
                            pass

                        break
                    else:
                        print("\nWrong command")
                        continue
                    

                print("\nWhat would you further want to know about?\n")
                sleep(1)

                break

            elif command == "3":
                spoofing()
                break
            else:
                print("\nInvalid command")
        
            if len(not_learnt) == 0:
                print("\nYou have learnt all the attacks! \n")
                break
        
    


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
    
    else:
        print("\nInvalid choice")
        tutorial()

    return()


#tutorial()
hack()