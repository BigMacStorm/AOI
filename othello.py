print "~Othello~"

def makeMove(player):
    coordList = raw_input("Enter coordinate for move (row col): ").split()
    coord = {'i': int(coordList[0]), 'j': int(coordList[1])}
    print "Player %d chose (%d, %d)" %(player, coord['i'], coord['j'])

    # Modify the board here

    if playerWins(player):
        print "Player %d wins!" %(player)

def playerWins(player):
    # stub
    return False

makeMove(0)
