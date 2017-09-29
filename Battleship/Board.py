# v 0.1  d 9/28/17
# TODO


class Board:
	def __init__(self, sizeX, sizeY):
		self.boardP1 = [[] * sizeY for x in range(sizeX)]
		self.boardP2 = [[] * sizeY for x in range(sizeX)]

		self.shipLayerP1 = self.boardP1
		self.shipLayerP2 = self.boardP2

		self.shotLayerP1 = self.boardP1
		self.shotLayerP2 = self.boardP2

	def reset(self):
		self.boardP1[:][:] = None
		self.boardP2[:][:] = None

	def shipType(self, x, y, player):
		if player == 1:
			return self.shipLayerP1[y][x]
		if player == 2:
			return self.shipLayerP2[y][x]
