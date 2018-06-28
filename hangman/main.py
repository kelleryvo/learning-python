import game
import random
import getpass
import time
# import player

# Defined Global variables
rounds = int()
player1name = ""
player2name = ""
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
    # threading.Timer(5.0, welcomeToHangman).start()
    print("Welcome to Hangman")
    for hangmanPart in hangman:
        time.sleep(0.25)
        print(hangmanPart)
    print("")
    print("")
    print("")


def playerGiveNames():
    player1name = raw_input("Type in a very flamboyant name: ")
    player2name = raw_input("Type in an even more flamboyant name: ")

    print("")
    print("")

def roundCheck():
    rounds = input("How many rounds would you like to play? ")
    while rounds >= 10:
        print("The number is higher than 10 or not a number at all")
        rounds = input("How many rounds would you like to play? ")

def gameProcedure():
    print("Prepare to get hanged " + player1name + " and " + player2name)
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
