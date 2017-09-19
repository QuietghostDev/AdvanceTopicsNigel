#v 0.1  d 9/18/17
#TODO Add ship locations

class Ship:
	def __init__(self, size, locX, locY):
		self.size = size
		self.isHit = [False for i in range(size)]

		self.x = locX
		self.y = locY

	def hit(self, index, isHit):
		self.isHit.pop(index)
		self.isHit.insert(index, True)
		return self.isHit

class Battleship(Ship):
	def __init__(self):
		#super(Battleship, self).__init__(4)
		Ship.__init__(4) #This should work

class Submarine(Ship):
	def __init__(self):
		Ship.__init__(3)

class Carrier(Ship):
	def __init__(self):
		Ship.__init__(5)


class Cruiser(Ship):
	def __init__(self):
		Ship.__init__(3)


class Destoryer(Ship):
	def __init__(self):
		Ship.__init__(2)
