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
			print "Player 0: %d -- Player 1: %d" %(self.board.count(True), self.board.count(False))
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
				if moveGood != True and self.playerIsHuman[player] == True:
					print "Invalid move."
			self.board.changePlayer()
			print "Player %d chose (%d, %d)" %(player, coord['i'], coord['j'])
			self.board.update()

		self.board.write()
		print "Player 0: %d -- Player 1: %d" %(self.board.count(True), self.board.count(False))
		print "Game over"
		player0Score = self.board.count(True)
		player1Score = self.board.count(False)
		winner = 0 if (player0Score > player1Score) else 1
		print "Player %d wins!" %(winner)

	def getHumanCoord(self):
		coordList = raw_input("Enter coordinate for move (row col): ").split()
		coord = {'i': int(coordList[0]), 'j': int(coordList[1])}
		return coord

	def getCompCoord(self):
		# The AI's not very smart yet
		return {'i': random.randint(0,7), 'j': random.randint(0,7)}
