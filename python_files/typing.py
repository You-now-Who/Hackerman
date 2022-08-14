from ast import While
from multiprocessing import current_process
from time import sleep
import time
import random
import os

from colorama import init
from termcolor import colored


def words():
    with open("python_files\words.txt", "r", encoding='utf-8') as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    return random.choice(words)
    
def begin_game(s_time):
    score=0
    while (time.time()-s_time) <= 60:
        x=words()
        print("Type the word: '" + colored(x, "blue") + "' :")
        ans=input()
        if ans==x:
            print(colored("Score +1 ", "green"))
            score=score+1
        else:
            print(colored("Wrong, try again ", "red"))
    return score


def typing_game():

    scanf=input("To start the game type '" + colored("s", "red")+ "': ")
    if scanf=='s' or scanf=='S':
        s_time=time.time()
        score=begin_game(s_time)

    return(score)