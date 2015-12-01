import numpy as np

class board:
	data = np.zeros((8,8), dtype=np.int)
	currentMove = True
	
	def init(self):
		data[3][3] = 1
		data[4][4] = 1
		data[3][4] = 2
		data[4][3] = 2
		print(data)
		
	def makeMove(self, x, y):
		if data[x][y] == 0:
			if currentMove:
				data[x][y] = 1
			else:
				data[x][y] = 0
			currentMove = not currentMove
			return True
		else:
			return False
			
	def done(self):
		for x in range(0,7):
			for y in range(0,7):
				if data[x][y] == 0:
					return False
		return True
		
	def update(self):
		pass
		