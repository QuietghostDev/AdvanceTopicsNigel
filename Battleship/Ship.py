#v 0.1  d 9/18/17
#TODO Use Python 3...

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
	def __init__(self, x, y):
		super(Battleship, self).__init__(4, x, y)
		#Ship.__init__(4)

class Submarine(Ship):
	def __init__(self, x, y):
		super(Submarine, self).__init__(3, x, y)
		#Ship.__init__(3)

class Carrier(Ship):
	def __init__(self, x, y):
		super(Carrier, self).__init__(5, x, y)
		#Ship.__init__(5)

class Cruiser(Ship):
	def __init__(self,x, y):
		super(Cruiser, self).__init__(3, x, y)
		#Ship.__init__(3)

class Destoryer(Ship):
	def __init__(self, x, y):
		super(Destoryer, self).__init__(2, x, y)
		#Ship.__init__(2)

cruiser1 = Cruiser(5,8)
print cruiser1.x
print cruiser1.y
print cruiser1.isHit
print cruiser1.size
