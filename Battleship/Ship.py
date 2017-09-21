# v 0.1  d 9/18/17
# TODO Use Python 3...


class Ship:
	def __init__(self, size, locX, locY, orient):
		self.size = size
		self.isHit = [False for i in range(size)]
		self.orientation = orient

		self.x = locX
		self.y = locY

	def hit(self, index):
		self.isHit.pop(index)
		self.isHit.insert(index, True)
		return self.isHit

	def getType(self):
		return self.__class__.__name__

	def placeShip(self):
		pass


class Battleship(Ship):
	def __init__(self, x, y):
		super(Battleship, self).__init__(4, x, y)
		# Ship.__init__(4)


class Submarine(Ship):
	def __init__(self, x, y):
		super(Submarine, self).__init__(3, x, y)
		# Ship.__init__(3)


class Carrier(Ship):
	def __init__(self, x, y):
		super(Carrier, self).__init__(5, x, y)
		# Ship.__init__(5)


class Cruiser(Ship):
	def __init__(self, x, y):
		super(Cruiser, self).__init__(3, x, y)
		# Ship.__init__(3)


class Destroyer(Ship):
	def __init__(self, x, y):
		super(Destroyer, self).__init__(2, x, y)
		# Ship.__init__(2)


battleship1 = Battleship(5, 8)
print(battleship1.x)
print(battleship1.y)
print(battleship1.getType())
print(battleship1.isHit)
print(battleship1.size)
