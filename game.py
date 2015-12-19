import board
import random

class Game:
	def __init__(self, numPlayers):
		self.playerIsHuman = [False, False]
		for i in range(0, numPlayers):
			self.playerIsHuman[i] = True

		self.board = board.board()

	def play(self):
		player = 1
		while True:
			if self.board.possible() != True:
				self.board.changePlayer()
				if(self.board.possible() != True):
					break
				continue

			self.board.write()
			print "Player 1: %d -- Player 2: %d" %(self.board.count(True), self.board.count(False))
			player = 0 if (player == 1) else 1

			if not self.board.possible():
				print "No possible moves, skipping your turn"
				continue

			moveGood = False
			while moveGood != True:
				coord = {}
				if self.playerIsHuman[player] == True:
					coord = self.getHumanCoord()
				else:
					coord = self.getCompCoord()
				moveGood = self.board.makeMove(coord['i'], coord['j'])
				if moveGood != True:
					if coord['i'] == -1 and coord['j'] == -1:
						print "Human player has chosen to skip their turn"
						break
					print "Invalid move."
			print "Player %d chose (%d, %d)" %(player+1, coord['i'], coord['j'])
			self.board.update()
			self.board.changePlayer()

		self.board.write()
		print "Player 1: %d -- Player 2: %d" %(self.board.count(True), self.board.count(False))
		print "Game over"
		player0Score = self.board.count(True)
		player1Score = self.board.count(False)
		winner = 0 if (player0Score > player1Score) else 1
		print "Player %d wins!" %(winner+1)

	def getHumanCoord(self):
		coordList = raw_input("Enter coordinate for move (row col): ").split()
		coord = {'i': int(coordList[0]), 'j': int(coordList[1])}
		return coord

	def getCompCoord(self):
		# The AI's kinda smart
		#the value passed into the handler is the desired depth
		move = self.minimaxHandler(3)
		print "Making move %d,%d with score %d" %(move[0][0], move[0][1], move[1])
		return {'i': move[0][0], 'j': move[0][1]}

	#hueristic function that will score the board for the current plauyer.
	#returns the score for the current player so will need to handle that
	#inside of the minimax recursive function
	#current algorithm is three fold:
	#1. Count the number of pieces
	#2. Give extra points to the pieces in the corner
	#3. Count the number of available moves
	def evaluate(self, sentBoard):
		score = 0
		temp = 0
		compare = 1
		if not sentBoard.currentMove:
			compare = 2
		for x in range(0,8):
			for y in range (0,8):
				if sentBoard.data[x][y] == 0:
					continue
				temp = 1
				if x == 0 and y == 0 or \
				x == 7 and y == 0 or \
				x == 7 and y == 7 or \
				x == 0 and y == 7:
					temp += 10
				#if it equals the current player
				if sentBoard.data[x][y] == compare:
					score += temp
				else:
					score -= temp
		ownMoveCount = sentBoard.getMoveCount(compare)
		compare = 1 if (sentBoard.currentMove == False) else 2
		enemyMoveCount = sentBoard.getMoveCount(compare)
		#score += ((ownMoveCount - enemyMoveCount) * 100)
		score += ownMoveCount *5

		return score

	def minimaxHandler(self, depth):
		moves = self.board.getMoveList()
		bestMove = [None, -999999999]
		simMove = [None, 0]
		for x in moves:
			simBoard = board.board(self.board)
			simBoard.makeMove(x[0], x[1])
			simBoard.changePlayer()

                        simMove[0] = [0,0,0]
			simMove[0][0] = x[0]
			simMove[0][1] = x[1]

			simMove[1] = self.minimaxRecurse(simBoard, depth-1)
			simMove[1] *= -1

			if simMove[1] > bestMove[1]:
				bestMove[0] = simMove[0]
				bestMove[1] = simMove[1]
		return bestMove

	def minimaxRecurse(self, simBoard, depth):
		if depth == 0 or not simBoard.possible():
			return self.evaluate(simBoard)
		moves = simBoard.getMoveList()
		bestScore = -999999999
		currentScore = 0
		for x in moves:
			simBoard = board.board(simBoard)
			simBoard.makeMove(x[0], x[1])
			simBoard.changePlayer()

			currentScore = self.minimaxRecurse(simBoard, depth-1)
			currentScore *= -1

			if currentScore > bestScore:
				bestScore = currentScore
		return bestScore
