#v 0.1  d. 9/18/17

class Ship:

	def __init__(self, size):
		self.size = size
		self.isHit = [False for i in range(size)]
	
	def hit(index, isHit):
		isHit.pop(index)
		isHit.insert(index, True)
		return isHit

		
class Battleship(Ship):

	def __init__(self):
		Ship.__init__(4)
		
		
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
