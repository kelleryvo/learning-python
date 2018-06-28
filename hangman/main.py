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
        time.sleep(0.05)
        print(hangmanPart)
    print("")
    print("© by Jason Millsom and Yvo Keller")
    print("")


def playerGiveNames():
    # Receive User Names
    playerOne = player.Player(raw_input("Type in a very flamboyant name: "), 1)
    playerTwo = player.Player(raw_input("Type in an even more flamboyant name: "), 2)

    print("")
    print("")

def roundCheck():
    rounds = input("How many rounds would you like to play? ")
    while rounds >= 10:
        print("The number is higher than 10 or not a number at all")
        rounds = input("How many rounds would you like to play? ")

def gameProcedure():
    # Receive User Names
    playerOne = player.Player(raw_input("Type in a very flamboyant name: "), 1)
    playerTwo = player.Player(raw_input("Type in an even more flamboyant name: "), 2)

    print("")
    print("")

    # Round Check
    rounds = input("How many rounds would you like to play? ")
    while rounds >= 10:
        print("The number is higher than 10 or not a number at all")
        rounds = input("How many rounds would you like to play? ")
    print("")
    print("")

    gameInstance = game.Game(rounds)

    # --
    print("Prepare to get hanged, " + playerOne.name + " and " + playerTwo.name + "! (•̀ᴗ•́)و ̑̑")
    print("")
    print("")

    # Choose Beginner with Random
    playerFirst = None
    playerSecond = None

    number = random.randint(1,2)
    if number == 1:
        playerFirst = playerOne
        playerSecond = playerTwo
    elif number == 2:
        playerFirst = playerTwo
        playerSecond = playerOne

    # Start game
    print("Alea iacta est - " + playerFirst.name + " begins!")
    print("")
    print("")
    time.sleep(1)

    # Loop for rounds
    i = 0
    while i < (gameInstance.rounds):
        i += 1

        if i > 1:
            # Change roles
            playerStore = playerFirst
            playerFirst = playerSecond
            playerSecond = playerStore

        print("// Round " + str(i) + " //")
        time.sleep(0.25)

        word = getpass.getpass(playerFirst.name + ", type in a word: ")
        gameInstance.setCurrentWord(word)
        print("")
        print("")

        # Loop for guesses
        x = 1
        while x < 10:
            x += 1

            # Guess Word
            print(playerSecond.name + ", guess this: " + gameInstance.showHint(x))
            answer = str(raw_input()).lower()

            if answer == gameInstance.currentWord:
                print("")
                print("Correct")
                print("")

                playerSecond.updateScore()

                break
            else:
                print("")
                print("Wrong")
                print("")

# run Program procedure
welcomeToHangman()
#playerGiveNames()
#roundCheck()
gameProcedure()
