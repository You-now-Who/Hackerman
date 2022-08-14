from ast import While
from multiprocessing import current_process
from time import sleep
import time
import random
import os

from colorama import init
from termcolor import colored

def init_hangman(word_passed):
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants"]
    word = word_passed
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 10
    guess = input("This is the encoded word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()


    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 10:

            time.sleep(1)
            print(colored("Wrong guess. The attack was unsuccessful!!!", "red") + "\n")
            print("The word was:",already_guessed,word)
            return(False)

            

        else:
            time.sleep(1)
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")


    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        return(True)

    elif count != limit:
        return(hangman())
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Scramble
def jumble(word):
    # sample() method shuffling the characters of the word
    random_word = random.sample(word, len(word))
 
    # join() method join the elements
    # of the iterator(e.g. list) with particular character .
    jumbled = ''.join(random_word)
    return jumbled
 

#Function for scramble game
def scramble(word):
    scrambled = jumble(word)
    print("The jumbled word is: ",scrambled)
    choice = input("Identify the word: ")
    if choice == word:
        print("You have guessed the word correctly!")
        return(True)
    else:
        print("You have guessed the word incorrectly!")
        return(False)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Function for memory game
def memory():
    open = random.randint(1,4)
    gates = [1,2,3,4]

    if open == 1:
        print("1: " + colored("Open", "green") + "\n2: " + colored("Closed", "red") + "\n3: " + colored("Closed", "red") + "\n4: " + colored("Closed", "red"))
    if open == 2:
        print("1: " + colored("Closed", "red") + "\n2: " + colored("Open", "green") + "\n3: " + colored("Closed", "red") + "\n4: " + colored("Closed", "red"))
    if open == 3:
        print("1: " + colored("Closed", "red") + "\n2: " + colored("Closed", "red") + "\n3: " + colored("Open", "green") + "\n4: " + colored("Closed", "red"))
    if open == 4:
        print("1: " + colored("Closed", "red") + "\n2: " + colored("Closed", "red") + "\n3: " + colored("Closed", "red") + "\n4: " + colored("Open", "green"))
    print("\n")
    sleep(1.75)
    os.system("cls")
    print("Which gate was open?")
    choice = int(input("1, 2, 3, or 4: "))
    if choice == open:
        print("You have guessed the word correctly!")
        return(True)
    else:
        print("You have guessed the word incorrectly!")
        return(False)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------