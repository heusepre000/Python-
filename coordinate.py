class Coordinate:
    x = -1
    y = -1
    letter = ""

    def __init__(self, X, Y, Letter):
      """When we create a new coordinate, this is the method that gets called to make it"""
      self.x = X
      self.y = Y 
      self.letter = Letter

    def __repr__(self):
      """This function defines what happens when we call print() on our object."""
      return "(" + self.letter + str(self.y + 1) + ")"