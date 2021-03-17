class Piece(object):
  owner = None
  piece_type = ""
  color = ""
  point_value = - 1
  valid_moves = []
  location = None

  def __init__(self, Location, Owner, Point_Value, Piece_Type, Valid_Moves, Color):
    self.location = Location
    self.owner = Owner
    self.color = Color
    self.point_value = Point_Value
    self.valid_moves = Valid_Moves
    
  def move(self, target, direction=None):
    pass

  def captured(self):
    self.owner.points += self.point_value