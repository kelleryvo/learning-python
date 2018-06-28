#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import getpass
import time

import game
import player

# Defined Global variables
rounds = int()
playerOne = None
PlayerTwo = None

hangman = [
"   ____",
"  |    |",
"  |    o",
"  |   /|\ ",
"  |    |",
"  |   / \ ",
" _|_",
"|   |______",
"|          |",
"|__________|"
]

# Defined Functions
def welcomeToHangman():
    # Print Welcome Message
    print("Welcome to Hangman")
    for hangmanPart in hangman:
        time.sleep(0.1)
        print(hangmanPart)
    print("")
    print("© by Jason Millsom and Yvo Keller")
    print("")


def playerGiveNames():
    playerOne = player.Player(raw_input("Type in a very flamboyant name: "), 1)
    PlayerTwo = player.Player(raw_input("Type in an even more flamboyant name: "), 2)

    print("")
    print("")

def roundCheck():
    rounds = input("How many rounds would you like to play? ")
    while rounds >= 10:
        print("The number is higher than 10 or not a number at all")
        rounds = input("How many rounds would you like to play? ")

def gameProcedure():
    print("Prepare to get hanged, " + playerOne.name + " and " + playerTwo.name)
    print("")
    print("")

    gameProcess = game.Game(rounds)

    for number in range(1):
        number = random.randint(1,2)
        if number == 1:
            word = getpass.getpass(player1name + " type in a word: ")
            word = word.lower()
            print(word)
        elif number == 2:
            word = getpass.getpass(player2name + " type in a word: ")
            word = word.lower()
            print(word)



# run Program procedure
welcomeToHangman()
playerGiveNames()
roundCheck()
gameProcedure()
