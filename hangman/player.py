class Player:
    def __init__(self, name, playerTurn):
        self.name = name
        self.playerTurn = playerTurn

        self.score = 0

    def updateScore(self):
        self.score += 1
        print(self.name + ", your new score is " + str(self.score) + "!")
        print("")
        print("")
