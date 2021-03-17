class Vector():
  x = 100
  y = 100
  valid_inputs = [-1, 0, 1]
  
  def __init__(self, X, Y):
  	if X not in self.valid_inputs:
  	    raise ValueError('Vector recieved an invalid x coordinates')
  	if Y not in self.valid_inputs:
  	    raise ValueError('Vector recieved an invalid y coordinates')
  	self.x = X
  	self.y = Y