from ast import While
from time import sleep

from colorama import init
from termcolor import colored

def login():
    print("\nGetting login details...")
    sleep(0.2)
    print("Enter Username: ")
    username = input()
    print("Enter Password: ")
    password = input()
    print("\nLogin successful.\n") 

def register():
    print("Register")

def initialise():
    print("Initialising...")
    sleep(2)
    print("Initialisation complete. \n")
    sleep(0.5)
    
    while True:
        print("Hello, and welcome to the world of hacker! \nWould you like to login or register?")
        print(colored("1. Login", 'green') + "\n" + colored("2. Register", 'yellow') + "\n" + colored("3. Exit", 'red'))
        choice = input("Enter your choice: ")
        if choice == "1":
            login()
            break
        elif choice == "2":
            register()
            break
        elif choice == "3":
            exit()
        else:
            print("\nInvalid choice. Kindly enter again.\n")
            sleep(1)



def main():
    initialise()

if __name__ == "__main__":
    main()