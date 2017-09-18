#v 0.1  d. 9/18/17

class Ship:
	def hit(index, isHit):
		isHit.pop(index)
		isHit.insert(index, False)
		return isHit

class Battleship(Ship):
	def __init__(self):
		size = 4

class Submarine(Ship):
	def __init__(self):
		size = 3

class Carrier(Ship):
	def __init__(self):
		size = 5

class Cruiser(Ship):
	def __init__(self):
		size = 3

class Destoryer(Ship):
	def __init__(self):
		size = 2
