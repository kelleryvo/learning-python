from random import randint

class Game:
    def __init__(self, rounds):
        self.rounds = rounds
        self.currentWord = ""
        self.currentWordList = []
        self.currentWordListHidden = []

    def printCurrentWord(self):
        print("Current word is " + self.currentWord)

    def setCurrentWord(self, currentWord):
        self.currentWord = currentWord.lower()

        for letter in self.currentWord:
            self.currentWordList.append(letter + " ")

        for letter in self.currentWord:
            if letter != " ":
                self.currentWordListHidden.append("- ")
            else:
                self.currentWordListHidden.append("  ")

    def showHint(self, progress):
        chances = [4, 10, 9, 8, 4, 6, 5, 4, 3, 2]
        
        i = 0
        while i < (len(self.currentWordListHidden) - 1):
            i += 1

            random = randint(1, chances[progress - 1])
            if random == 1:
                self.currentWordListHidden[i] = self.currentWordList[i]

        # Build String and Print hidden word
        hiddenWord = ""
        for letter in self.currentWordListHidden:
            hiddenWord += letter

        print("Guess this: " + hiddenWord)
