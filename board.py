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
			
	def movePoint(self, point, direction):
		if direction == 0:
			point[0] += 1
		elif direction == 1:
			point[0] += 1
			point[1] += 1
		elif direction == 2:
			point[1] += 1
		elif direction == 3:
			point[0] -= 1
			point[1] += 1
		elif direction == 4:
			point[0] -= 1
		elif direction == 5:
			point[0] -= 1
			point[1] -= 1
		elif direction == 6:
			point[0] -= 1
		elif direction == 7:
			point[0] += 1
			point[1] -= 1
		return point
			
		
	def update(self):
		temp = self.data
		cursor = self.mostRecent
		goal = -1
		count = 0
		for x in range(0,7):
			count = 0
			goal = self.data[cursor[0]][cursor[1]]
			
			if goal == 1:
				goal == 2
			elif goal == 2:
				goal == 1
				
			cursor = self.mostRecent
			cursor = self.movePoint(cursor, x)
			if goal == -1:
				continue
				
			while self.data[cursor[0]][cursor[1]] == goal and (0 <= cursor[0] <= 7) and (0 <= cursor[1] <= 7):
				count += 1
				self.movePoint(cursor, x)
			
			if (0 <= cursor[0] <= 7) and (0 <= cursor[1] <= 7):
				continue
							
			cursor = mostRecent
			goal = self.data[cursor[0]][cursor[1]]
			cursor = self.movePoint(cursor, x)
			for y in range(0,count):
				temp[cursor[0]][cursor[1]] = goal
				cursor = self.movePoint(cursor, x)
				
		self.data = temp
			
				
				
			
			
			
		
		