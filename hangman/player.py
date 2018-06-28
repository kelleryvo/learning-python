class Player:
    def __init__(self, name, playerTurn):
        self.name = name
        self.playerTurn = playerTurn

        self.score = 0

    def updateScore(self, score):
        self.score = score
        print(self.name + ", your new score is " + str(self.score) + "!")
