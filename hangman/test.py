import game
import player

playerx = player.Player("Yvo", 0)
playerx.updateScore(0)
playerx.updateScore(4)

game1 = game.Game(3)
game1.printCurrentWord()

word = raw_input("Give me a Word: ")
print(word)
game1.setCurrentWord(word)
print(game1.currentWord)

i = 1
while i < 10:
    i += 1
    game1.showHint(i)
