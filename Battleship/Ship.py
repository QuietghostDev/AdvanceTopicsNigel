#v. 0.1  d. 9/18/17

class Ship:

	def hit(index, isHit):
		isHit.pop(index)
		isHit.insert(index, False)
		return isHit

	
