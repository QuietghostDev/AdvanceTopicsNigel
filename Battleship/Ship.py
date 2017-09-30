# v 0.1  d 9/28/17
# TODO


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

	def getIndex(self, x, y):
		if self.orientation == 0:
			return y-self.y
		if self.orientation == 1:
			return x-self.x


class Battleship(Ship):
	def __init__(self, x, y, orient):
		super(Battleship, self).__init__(4, x, y, orient)


class Submarine(Ship):
	def __init__(self, x, y, orient):
		super(Submarine, self).__init__(3, x, y, orient)


class Carrier(Ship):
	def __init__(self, x, y, orient):
		super(Carrier, self).__init__(5, x, y, orient)


class Cruiser(Ship):
	def __init__(self, x, y, orient):
		super(Cruiser, self).__init__(3, x, y, orient)


class Destroyer(Ship):
	def __init__(self, x, y, orient):
		super(Destroyer, self).__init__(2, x, y, orient)


class Water(Ship):
	def __init__(self, x, y):
		super(Water, self).__init__(1, x, y, 0)
