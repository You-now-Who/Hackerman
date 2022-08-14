import os
import time
from time import sleep
import random
from termcolor import colored

#Firebase initialisation
from unicodedata import name
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from python_files.typing import words, typing_game
from python_files.hangman import hangman, init_hangman, memory, scramble
import threading
  

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def start_game(user, mode):
    os.system('cls')
    player_is = "neutral"
    # print(mode)
    if mode == "offline":
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
        state = "not_scanned"

        while True:

            #print(state)

            if state == "not_scanned":
                available_commands = ["scan"]


            if state == "out_port":
                available_commands = []
                current_port = 0
                for port in ports:
                    available_commands.append( "cd " + str(port))
    
                print("\nPorts: ")
                for port in ports:
                    print(colored(port, "blue"), end="")
                    print("    ", end="")
                print("\n")

            if state == "in_port":
                available_commands = ["cd ..", "dos", "mitm", "malware"]
            
            command = input("\nEnter your command: ")

            if command in available_commands:

                if command.startswith("cd "):
                    #print(command[3:])
                    if command == "cd ..":
                        print("\nGoing back to all ports")
                        state = "out_port"

                    elif int(command[3:]) in ports:
                        current_port = int(command[3:])
                        print(colored("You have entered the port ", "green") + colored(current_port, "blue"))
                        state = "in_port"
                        

                elif command == "scan":
                    print(colored("Scanning ports...\n", "green"))
                    time.sleep(2)
                    state = "out_port"
                
                elif command == "dos":
                    print(colored("You have chosen to DOS the port ", "green") + colored(current_port, "blue"))
                    points = typing_game()

                    if points >= 20:
                        print("\nYou have " + colored("successfully", "green") + " hacked the system! \n")
                        print("\nYou have gained " + colored(points, "green") + " points! \n")
                        points = user.child("points").get()
                        user.update({"points": points})
                        break
                    else:
                        print(colored("\nYour attack was too slow, and the people were alerted \n", "red"))
                        break


                
                elif command == "mitm":
                    print(colored("You have chosen to MITM the port ", "green") + colored(current_port, "blue"))
                    
                    print("You get this encoded message")
                    init_hangman(words())
                    result = hangman()

                    if result == True:
                        print("\nYou have successfully decoded the message! \n")
                        points = (random.randint(30,50))
                        print("\nYou have gained " + colored(points, "green") + " points! \n")
                        points = user.child("points").get()
                        user.update({"points": points})
                        break
                    else:
                        print("\nYou have failed to decode the message! \n")
                        break

                elif command == "malware":
                    print(colored("You have chosen to install malware on the port ", "green") + colored(current_port, "blue"))
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
                    
                    s_time=time.time()

                    while (time.time()-s_time) <= 120:
                        word = words()
                        a = scramble(word)
                        if a == True:
                            progress += random.randint(20,30)
                            if(progress >= 100):
                                print(colored("You have successfully installed malware", "green"))
                                points = random.randint(60, 70)
                                points = user.child("points").get()
                                user.update({"points": points})
                                print(colored("You recieved " + str(points) + " points", "green"))
                                return()
                            else:
                                print("Malware installation: " + colored(progress, "green") + "%")
                        else:
                            print("\nThe scramble was wrong. The correct word was " + word + "\n")
                    
                

            else:
                print(colored("Invalid command\n", "red"))
                sleep(0.4)
                print("Here are the list of available commands: ")
                for c in available_commands:
                    sleep(0.1)
                    print(colored(c, "yellow"))

                continue

#----------------------------------------------------------------------------------------------------------------------------------------------------

    elif player_is == "security":
        print(colored("You are the cyberpolice", "green"))
        print("Objective: Protect all the ports for 4 minutes")

        ports = []
        for i in range(4):
            ports.append(random.randint(1000,9999))

        available_commands = []
        state = "not_scanned"

        while True:

            #print(state)

            if state == "not_scanned":
                available_commands = ["scan"]


            if state == "out_port":
                available_commands = []
                current_port = 0
                for port in ports:
                    available_commands.append( "cd " + str(port))
    
                print("\nPorts: ")
                for port in ports:
                    print(colored(port, "blue"), end="")
                    print("    ", end="")
                print("\n")

            if state == "in_port":
                available_commands = ["cd ..", "check"]
            
            command = input("\nEnter your command: ")

            if command in available_commands:

                if command.startswith("cd "):
                    #print(command[3:])
                    if command == "cd ..":
                        print("\nGoing back to all ports")
                        state = "out_port"

                    elif int(command[3:]) in ports:
                        current_port = int(command[3:])
                        print(colored("You have entered the port ", "green") + colored(current_port, "blue"))
                        state = "in_port"
                        

                elif command == "scan":
                    print(colored("Scanning ports...\n", "green"))
                    time.sleep(2)
                    state = "out_port"

                elif command == "check":
                    if random.randint(1,5) == 4:
                        print("This port is being" +  colored("attacked!", "red"))
                        type_threat = random.randint(1,3)
                        if type_threat == 1:
                            print("The type of attack is " + colored("DoS", "red"))
                        
                            points = typing_game()
                            
                            if points >= 20:
                                print("\nYou have " + colored("successfully", "green") + " protected the system! \n")
                                print("\nYou have gained " + colored(points, "green") + " points! \n")
                                points = user.child("points").get()
                                user.update({"points": points})
                                break
                            else:
                                print(colored("\nYour defense was too slow, and the system was hacked \n", "red"))
                                break

                        if type_threat == 2:
                            print("The type of attack is " + colored("MITM", "red"))

                            print("You get this encoded message. Enter letters to decode it.")
                            init_hangman(words())
                            result = hangman()

                            if result == True:
                                print("\nYou have successfully decoded the message! \n")
                                points = (random.randint(30,50))
                                print("\nYou have gained " + colored(points, "green") + " points! \n")
                                points = user.child("points").get()
                                user.update({"points": points})
                                break
                            else:
                                print("\nYou have failed to decode the message, and the system was hacked!\n")
                                break

                        if type_threat == 3:
                            print("The type of attack is " + colored("Malware", "red"))
                            print("To stop the attack, you will need to unscramble these code words")
                            s_time=time.time()

                            while (time.time()-s_time) <= 120:
                                word = words()
                                a = scramble(word)
                                if a == True:
                                    progress += random.randint(20,30)
                                    if(progress >= 100):
                                        print(colored("You have successfully installed malware", "green"))
                                        points = random.randint(60, 70)
                                        points = user.child("points").get()
                                        user.update({"points": points})
                                        print(colored("You recieved " + str(points) + " points", "green"))
                                        return()
                                    else:
                                        print("Malware uninstallation: " + colored(progress, "green") + "%")
                                else:
                                    print("\nThe scramble was wrong. The correct word was " + word + "\n")
                            else:
                                print(colored("You were unable to decode them, and your pc was hacked", "red"))
                        
                        else:
                            print("This port is " + colored("secure", "green"))
                    
                

            else:
                print(colored("Invalid command\n", "red"))
                sleep(0.4)
                print("Here are the list of available commands: ")
                for c in available_commands:
                    sleep(0.1)
                    print(colored(c, "yellow"))

                continue



    elif mode == "online":
        print("This feature is not yet available")

    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def play_screen(user):
    while True:

        print("\nWhat would you like to do?")
        print(colored("1. Play Offline", 'green') + "\n" + colored("2. Play Online", 'blue') + "\n" + colored("3. Exit", 'red'))
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nYou are playing offline")
            return("offline")
        elif choice == "2":
            print("This feature is not yet available")
            continue
        elif choice == "3":
            print("\nExiting...")
            exit()
        else:
            print(colored("Invalid choice", "red"))
            continue



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def play(user):

    mode = play_screen(user)
    start_game(user, mode)
    #Reached this point if user wants to play offline
    
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
# play(None)