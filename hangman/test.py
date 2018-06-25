import game

game1 = game.Game(3)
game1.printCurrentWord()
game1.currentWord = raw_input("Give me a Word: ")
game1.showHint()
