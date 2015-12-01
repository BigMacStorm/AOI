print "~Othello~"

coordList = raw_input("Enter coordinate for move (row col): ").split()
coord = {'i': int(coordList[0]), 'j': int(coordList[1])}
print "Player chose coordinate (%d, %d)" %(coord['i'], coord['j'])
