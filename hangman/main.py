#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import getpass
import time

import game
import player
import colors

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
"|__________|"
]

# Defined Functions
def checkOdd(x):
    if x % 2: #ungrade
        print("ungerade")
        return true
    else: #grade
        print("gerade")
        return false

def welcomeToHangman():
    #variables
    col = colors.Colors

    # Print Welcome Message
    print(col.BOLD)
    print("Welcome to Hangman!")
    for hangmanPart in hangman:
        time.sleep(0.05)
        print(hangmanPart)
    print("")
    print("© by Jason Millsom and Yvo Keller")
    print("")
    print(col.ENDC)

def gameProcedure():
    #variables
    col = colors.Colors

    # Receive User Names
    playerOne = player.Player(raw_input("Type in a very flamboyant name: "))
    playerTwo = player.Player(raw_input("Type in an even more flamboyant name: "))

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

        filledHangman = []

        if i > 1:
            # Change roles
            playerStore = playerFirst
            playerFirst = playerSecond
            playerSecond = playerStore

        print(col.BOLD + "Round " + str(i) + col.ENDC)
        time.sleep(0.1)

        word = getpass.getpass(playerFirst.name + ", type in a word: ")
        gameInstance.setCurrentWord(word)
        print("")
        print("")

        # Loop for guesses
        x = 0
        while x < 10:
            x += 1

            # Guess Word
            print(playerSecond.name + ", guess this: " + gameInstance.showHint(x))
            answer = str(raw_input()).lower()

            if answer == gameInstance.currentWord:
                print("")
                print(col.OKGREEN + "Correct! This round goes to you, " + playerSecond.name + col.ENDC)
                print("")

                playerSecond.updateScore()

                break
            else:
                filledHangman.append(hangman[x - 1])

                print("")
                for element in filledHangman:
                    print(element)

                print("")

                if x == 10:
                    playerFirst.updateScore()
                    print("")
                    print("You got hanged, " + playerSecond.name + "... The word was " + gameInstance.currentWord)
                    print("")
                    print(col.FAIL + "This round goes to " + playerFirst.name + col.ENDC)
                    print("")

    # Print Results
    print(col.HEADER + col.UNDERLINE + "Final Stats:" + col.ENDC)
    print(playerFirst.name + " - " + str(playerFirst.score) + " points.")
    print(playerSecond.name + " - " + str(playerSecond.score) + " points")
    print("")

    if playerFirst.score > playerSecond.score:
        print(col.OKGREEN + "Congrats, " + playerFirst.name + ", you won this game!" + col.ENDC)
    else:
        print(col.OKGREEN + "Congrats, " + playerSecond.name + ", you won this game!" + col.ENDC)

    print("")
    print("Until next time!")
    print("")

# run Program procedure
welcomeToHangman()
gameProcedure()
