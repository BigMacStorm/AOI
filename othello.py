import board

class Game:
    def __init__(self, numPlayers):
        self.playerIsHuman = [False, False]
        for i in range(0, numPlayers):
            self.playerIsHuman[i] = True

        self.myboard = board.board()

    def play(self):
        player = 1
        while self.playerWins(player) != True:
            player = 0 if (player == 1) else 1
            self.makeMove(player)

        print "Player %d wins!" %(player)

    def makeMove(self, player):
        coordList = raw_input("Enter coordinate for move (row col): ").split()
        coord = {'i': int(coordList[0]), 'j': int(coordList[1])}
        print "Player %d chose (%d, %d)" %(player, coord['i'], coord['j'])

        # Modify the board here

    def playerWins(self, player):
        # stub
        return False

# Main program
print "~Othello~"
numPlayers = int(raw_input("Number of players (0-2): "))
game = Game(numPlayers)
game.play()
