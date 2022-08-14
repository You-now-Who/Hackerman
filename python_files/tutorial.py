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
from python_files.hangman import hangman, init_hangman, memory, scramble



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Hack tutorial
def hack(other_completed = False):
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
    
    not_learnt = ["DoS", "MITM", "Malware"]

    while True:        
        
        if len(not_learnt) == 0:
                print("\nYou have learnt all the attacks! \n \n")
                sleep(2)
                break

        sleep(0.2)

        print("\nWhat attack do you want to learn about? \n" + colored("1. DoS", "blue") + " \n" + colored("2. MITM", "green") + " \n" + colored("3. Malware", "red"))

        print("How do you want to continue?")
        
        while True:
            command = input()

            # print(not_learnt)
            # print("command = " + command)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
                    not_learnt.remove("DoS")
                except KeyError:
                    pass

                print("\nWhat would you further want to know about?\n")
                sleep(1)
                
                break

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
                            not_learnt.remove("MITM")
                        except KeyError:
                            pass

                        break
                    else:
                        print("\nWrong command")
                        continue
                    

                print("\nWhat would you further want to know about?\n")
                sleep(1)

                break

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            elif command == "3":
                print("\nYou have chosen " + colored("Malware", "red") + ". Excellent choice. A Malware attack is a type of attack where a hacker  installs a malicious software on a system. This software is usually used to steal data from the victim. \n")
                print("\nYou can initiate a Malware attack on the port " + colored(current_port, "blue") + " by using the " + colored("malware", "red") + " command. \n")

                while True:
                    command = input("Initiate a Malware attack on port " + colored(current_port, "blue") + ": ")
                    if command == "malware":
                        print("\nInitiating Malware attack on port " + colored(current_port, "blue") + "...")
                        sleep(2)
                        print("\nMalware attack on port " + colored(current_port, "blue") + " has been initiated")
                        break
                    else:
                        print("\nWrong command")
                        continue
                print("To install the Malware, you need to firstly bypass the " + colored("firewall", "green") + ".\n")
                print("You will be shown " + colored("4 gates", "blue") + " for a short amount of time. You need to memorise in which gate is opened, and then enter that gate by typing the correspoding number\n")
                input("Press any key to continue...")

                a = memory()

                if a == True:
                    print(colored("\nYou have successfully bypassed the firewall! \n", "green"))
                    print("Starting malware installation\n")
                    sleep(0.3)
                else:
                    print(colored("\nYou have failed to bypass the firewall! \n", "red"))
                    break
                
                progress = 0
                print("\nNow to install the malware, you need to unscramble the " + colored("code", "red") + " that appears on the screen.\n")
                
                while True:
                    word = words()
                    a = scramble(word)
                    if a == True:
                        progress += random.randint(20,30)
                        if(progress >= 100):
                            print(colored("You have successfully installed malware", "green"))
                            break
                        else:
                            print("Malware installation: " + colored(progress, "green") + "%")
                    else:
                        print("\nThe scramble was wrong. The correct word was " + word + "\n")
                
                sleep(1)
                try:
                    not_learnt.remove("Malware")
                except KeyError:
                    pass
                
                print("\nWhat would you further want to know about?\n")

                break
            
            else:
                print("\nInvalid command")
        
    print("You can exit these ports by using the " + colored("cd ..", "red") + " command. Try using "  + colored("cd ..", "red") + " to exit port 4020" + " \n")
    sleep(0.4)
    while True:
        command = input("Use the cd.. command on port " + colored("4020", "blue") + ": ")
        if command == "cd ..":
            current_port = 4020
            print("\nYou have exited port " + colored(current_port, "blue") + " \n")
            break
        else:
            print("\nWrong command")
            continue
    
    current_port = 0
    for port in ports:
        print(colored(port, "blue"), end="")
        print("    ", end="")

    if other_completed == True:
        print("\n \n This concludes the tutorial. Would you want to learn about the" + " " + colored("secure", "blue") + " system now? \n")
        while True:
            command = input("Type " + colored("y", "red") + " to learn about the secure system, or type " + colored("n", "red") + " to exit the tutorial: ")
            if command == "yes":
                secure(True)
                break
            elif command == "no":
                break
            else:
                print("\nWrong command")
                continue

    else:
        print("\n \n This concludes the tutorial. Would you like to start the game? \n")    
        input("Press any key to continue...")
    

    return()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Secure tutorial
def secure(other_completed = False):
    print("\n Secure is the process of securing a system against the threats of a hacker. \n")
    sleep(0.4)

    print("In this game, there are various network " + colored("ports", "blue") + ". You need to check each port for threats\n")
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

    sleep(0.4)
    print("Now, you can check the port " + colored(current_port, "blue") + " for any sort of threats.\n You can do this by using the " + colored("check", "red") + " command.\n")
    sleep(0.4)
    while True:
        command = input("Check the port " + colored(current_port, "blue") + " by using the " + colored("check", "red") + " command: ")
        if command == "check":
            print("\nChecking port " + colored(current_port, "blue") + "...")
            sleep(2)
            print("\nPort " + colored(current_port, "blue") + " has been checked. No threats were found")
            break
        else:
            print("\nWrong command")
            continue
    
    print("This port is " + colored("secure", "green") + ". You need to check the other ports\n")

    print("\nYou can exit these ports by using the " + colored("cd ..", "red") + " command. Try using "  + colored("cd ..", "red") + " to exit port 4020" + " \n")
    sleep(0.4)
    while True:
        command = input("Use the cd.. command on port " + colored("4020", "blue") + ": ")
        if command == "cd ..":
            print("\nYou have exited port " + colored(current_port, "blue") + " \n")
            break
        else:
            print("\nWrong command")
            continue

    

    while True:
        current_port = 0
        print("\n Available ports: \n")
        
        for port in ports:
            print(colored(port, "blue"), end="")
            print("    ", end="")

        print("\n")
        while True:
            command = input("Enter your command: ")
            valid = False
            for port in ports:
                if command == "cd " + str(port):
                    current_port = port
                    print("\nYou have entered port " + colored(current_port, "blue") + " \n")
                    valid = True
                    break

            if valid == False:
                print("\nInvalid command")
                continue
            else:
                break

        while True:
            command = input("Enter your command: ")
            threat = "active"
            if command == "check":
                print("\nChecking port " + colored(current_port, "blue") + "...")
                sleep(2)
                if current_port == 1900:
                    print("\nPort " + colored(current_port, "blue") + " has been checked. A threat was found")
                    print("\nThe threat is " + colored("malware", "red") + " \n")
                    if secure_malware() == True:
                        threat = "deactive"
                        break
                else:
                    print("\nPort " + colored(current_port, "blue") + " has been checked. No threats were found")
                    print("This port is " + colored("secure", "green") + ". You need to check the other ports\n")
            
            elif command == "cd ..":
                print("\nYou have exited port " + colored(current_port, "blue") + " \n")

                break

            else:
                print("\nWrong command")
                continue

        if threat == "deactive":
            break
        
        print("This threat has been neutralized. However, in a real game, you need to constantly keep scanning the ports until the time doesnt run out \n")
        sleep(0.4)
        if other_completed == True:
            print("\nThis concludes the tutorial. Would you want to learn about the " + colored("hack", "red") + " system now? \n")
            while True:
                command = input("Type " + colored("y", "red") + " to learn about the hack system, or type " + colored("n", "red") + " to exit the tutorial: ")
                if command == "yes":
                    hack(True)
                    break
                elif command == "no":
                    break
                else:
                    print("\nWrong command")
                    continue
    

    return()    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Secure malware tutorial
def secure_malware():
    print("A malware is a program that is designed to steal or damage data.\n You need to stop this malware as fast as you can.\n")
    sleep(0.4)
    print("To stop the malware, you need to unscramble the incoming data.\n")

    input("Press any key to continue...")

    progress = 0
    while True:
        word = words()
        a = scramble(word)
        if a == True:
            progress += random.randint(20,30)
            if(progress >= 100):
                print(colored("You have successfully uninstalled malware", "green"))
                break
            else:
                print("Malware uninstallation: " + colored(progress, "green") + "%")
        else:
            print("\nThe scramble was wrong. The correct word was " + word + "\n")
            
    return(True)

    

    


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
        print("\nReturning to main screen...")
        sleep(1)
        os.system('cls')
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

    os.system('cls')
    print("Starting the game now...")
    sleep(1)
    os.system('cls')


    return()


#tutorial()
#hack()