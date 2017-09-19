#v 0.1  d 9/18/17
#TODO

class Board:

	def __init__(self, sizeX, sizeY):
		self.boardP1 = [[for y in range(sizeY)] for x in range(sizeX)]
		self.boardP2 = [[for y in range(sizeY)] for x in range(sizeX)]

	def reset(self): #Test this, I don't know if it works
		self.boardP1[:][:] = None
		self.boardP2[:][:] = None

	def initLayers(self): #Honestly I got to figure out the better way of doing this
		self.shipLayerP1 = self.boardP1
		self.shipLayerP2 = self.boardP2

		self.shotLayerP1 = self.boardP1
		self.shotLayerP2 = self.boardP2
