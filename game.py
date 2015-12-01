import board

class Game:
    def __init__(self, numPlayers):
        self.playerIsHuman = [False, False]
        for i in range(0, numPlayers):
            self.playerIsHuman[i] = True

        self.board = board.board()

    def play(self):
        player = 1
        while self.board.done() != True:
            player = 0 if (player == 1) else 1

            coord = {}
            if self.playerIsHuman[player] == True:
                coord = self.getHumanCoord()
            else:
                coord = self.getCompCoord()

            print "Player %d chose (%d, %d)" %(player, coord['i'], coord['j'])
            self.board.makeMove(coord['i'], coord['j'])
            self.board.update()

        print "Game over"
        player0Score = self.board.count(True)
        player1Score = self.board.count(False)
        winner = 0 if (player0Score > player1Score) else 0
        print "Player %d wins!" %(winner)

    def getHumanCoord(self):
        coordList = raw_input("Enter coordinate for move (row col): ").split()
        coord = {'i': int(coordList[0]), 'j': int(coordList[1])}
        return coord

    def getCompCoord(self):
        # The AI's not very smart yet
        return {'i': 0, 'j': 0}

    def playerWins(self, player):
        # stub
        return False
