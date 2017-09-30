# v 0.1  d 9/29/17
# TODO Write clone method


class Board:
	def __init__(self, sizeX, sizeY):
		self.shipLayerP1 = [[None] * sizeY for x in range(sizeX)]
		self.shipLayerP2 = [[None] * sizeY for x in range(sizeX)]

		self.shotLayerP1 = [[None] * sizeY for x in range(sizeX)]
		self.shotLayerP2 = [[None] * sizeY for x in range(sizeX)]

	def reset(self):
		self.board[:][:] = None

	def shipType(self, x, y, player):
		if player == 1:
			return self.shipLayerP1[y][x].getType()
		if player == 2:
			return self.shipLayerP2[y][x].getType()

	def clone(self):
		pass