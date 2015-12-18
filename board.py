#!/usr/bin/env python2.7
import numpy as np
import sys
import random

class board:

	def __init__(self, copy = None):
		self.data = np.zeros((8,8), dtype=np.int)
		self.currentMove = True
		self.mostRecent = [-1,-1]
		self.data[3][3] = 1
		self.data[4][4] = 1
		self.data[3][4] = 2
		self.data[4][3] = 2
		if copy != None:
			self.currentMove = copy.currentMove
			self.mostRecent = copy.mostRecent
			for x in range(0,8):
				for y in range(0,8):
					self.data[x][y] = copy.data[x][y]

	def makeMove(self, x, y):
		if (not self.check(x,y)):
			return False
		if self.data[x][y] == 0:
			if self.currentMove:
				self.data[x][y] = 1
			else:
				self.data[x][y] = 2
			self.mostRecent = [x,y]
			return True
		else:
			return False

	def done(self):
		for x in range(0,8):
			for y in range(0,8):
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
		for x in range(0,8):
			for y in range(0,8):
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
			point[1] -= 1
		elif direction == 7:
			point[0] += 1
			point[1] -= 1

	#updates the board
	def update(self):
		temp = self.data
		cursor = [self.mostRecent[0], self.mostRecent[1]]
		goal = -1
		count = 0
		for x in range(0,8):
			cursor = [self.mostRecent[0], self.mostRecent[1]]
			count = 0
			goal = self.data[cursor[0]][cursor[1]]

			if goal == 1:
				goal = 2
			elif goal == 2:
				goal = 1

			cursor = [self.mostRecent[0], self.mostRecent[1]]
			self.movePoint(cursor, x)
			if goal == 0:
				continue

			while (0 <= cursor[0] <= 7) and (0 <= cursor[1] <= 7) and self.data[cursor[0]][cursor[1]] == goal:
				count += 1
				self.movePoint(cursor, x)

			if (not (0 <= cursor[0] <= 7)) or (not (0 <= cursor[1] <= 7)) or self.data[cursor[0]][cursor[1]] != self.data[self.mostRecent[0], self.mostRecent[1]]:
				continue

			cursor = [self.mostRecent[0], self.mostRecent[1]]
			goal = self.data[cursor[0]][cursor[1]]
			self.movePoint(cursor, x)
			for y in range(0,count):
				temp[cursor[0]][cursor[1]] = goal
				self.movePoint(cursor, x)

		self.data = temp

	#prints the board out
	def write(self):
		for x in range(0,8):
                        print("%d|" %(x)),
			for y in range(0,8):
                                if self.data[x][y] == 0:
                                        print("-"),
                                else:
				        print(self.data[x][y]),
			print(" ")
                print("  "),
                for x in range(0,8):
                        print("_"),
                print ""
                print("  "),
                for x in range(0,8):
                        print("%d" %(x)),
		print(" ")
		print(" ")

	#returns a single bool on if a move is doable
	def check(self, xSent, ySent):
		if self.data[xSent][ySent] != 0:
			return False
		storage = self.data[xSent][ySent]
		temp = self.data
		cursor = [xSent, ySent]
		if self.currentMove:
			temp[xSent][ySent] = 1
		else:
			temp[xSent][ySent] = 2
		goal = -1
		count = 0
		for x in range(0,8):
			cursor = [xSent, ySent]
			goal = temp[cursor[0]][cursor[1]]
			count = 0

			if goal == 1:
				goal = 2
			elif goal == 2:
				goal = 1

			cursor = [xSent, ySent]
			self.movePoint(cursor, x)
			if goal == 0:
				continue

			while (0 <= cursor[0] <= 7) and (0 <= cursor[1] <= 7) and temp[cursor[0]][cursor[1]] == goal:
				count += 1
				self.movePoint(cursor, x)


			if (not (0 <= cursor[0] <= 7)) or (not (0 <= cursor[1] <= 7)) or temp[cursor[0]][cursor[1]] != temp[xSent, ySent]:
				continue

			if count > 0:
				self.data[xSent][ySent] = storage
				return True
		self.data[xSent][ySent] = storage
		return False

	def possible(self):
		compare = -1
		if self.currentMove:
			compare = 1
		else:
			compare = 2
		for x in range(0,8):
			for y in range(0,8):
				if self.data[x][y] == 0 and self.check(x, y):
					return True
		return False

	def getMoveCount(self, player):
		count = 0
		for x in range(0,8):
			for y in range(0,8):
				if self.check(x, y):
					count += 1
		return count


	def getMoveList(self):
		moveList = []
		counter = 0
		for x in range(0,8):
			for y in range(0,8):
				if self.check(x, y):
					moveList.append([x,y,counter])
					counter += 1
		#random.shuffle(moveList)
		return moveList

	def changePlayer(self):
		self.currentMove = not self.currentMove
