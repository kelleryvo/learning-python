class Game:
    def __init__(self, rounds):
        self.rounds = rounds
        self.currentWord = ""
        self.hiddenWord = ""

    def printCurrentWord(self):
        print("Current word is " + self.currentWord)
    def showHint(self):
        for letter in self.currentWord:
            self.hiddenWord += letter.replace(letter, "-")
        print("Guess this: " + self.hiddenWord)
