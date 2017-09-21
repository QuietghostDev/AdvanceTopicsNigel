# v 0.1  d 9/18/17
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

newBoard = Board(24, 12)
print(newBoard.boardP1)
print(newBoard.shipLayerP1)