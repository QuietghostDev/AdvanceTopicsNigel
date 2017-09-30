# v 0.1  d 9/28/17
# TODO


class Board:
	def __init__(self, sizeX, sizeY):
		self.board = [[None] * sizeY for x in range(sizeX)]

		self.shipLayerP1 = self.board
		self.shipLayerP2 = self.board

		self.shotLayerP1 = self.board
		self.shotLayerP2 = self.board

	def reset(self):
		self.board[:][:] = None

	def shipType(self, x, y, player):
		if player == 1:
			return self.shipLayerP1[y][x].getType()
		if player == 2:
			return self.shipLayerP2[y][x].getType()
