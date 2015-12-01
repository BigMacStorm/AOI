#!/usr/bin/env python2.7
import numpy as np

class board:
	data = np.zeros((8,8), dtype=np.int)
	currentMove = True
	mostRecent = (-1,-1)
	
	def __init__(self):
		self.data[3][3] = 1
		self.data[4][4] = 1
		self.data[3][4] = 2
		self.data[4][3] = 2
		
	def makeMove(self, x, y):
		if self.data[x][y] == 0:
			if self.currentMove:
				self.data[x][y] = 1
			else:
				self.data[x][y] = 2
			self.currentMove = not self.currentMove
			self.mostRecent = (x,y)
			return True
		else:
			return False
			
	def done(self):
		for x in range(0,7):
			for y in range(0,7):
				if self.data[x][y] == 0:
					return False
		return True
		
	def count(self, sent):
		compare = -1
		counter = 0
		if sent:
			compare = 1
		else:
			compare = 2		
		for x in range(0,7):
			for y in range(0,7):
				if self.data[x][y] == compare:
					counter += 1
		return counter
		
	def update(self):
		temp = self.data
		
		