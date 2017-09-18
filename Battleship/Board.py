#v. 0.1  d. 9/18/17

class Board:

	def __init__(self, sizeX, sizeY):
		self.boardP1 = [[for y in range(sizeY)] for x in range(sizeX)]
		self.boardP2 = [[for y in range(sizeY)] for x in range(sizeX)]

	def reset(self):
		self.boardP1[:][:] = None
		self.boardP2[:][:] = None
