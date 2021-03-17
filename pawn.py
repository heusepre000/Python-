import piece
import vector

class Pawn(piece.Piece):
    has_moved = False
    num_movable_squares = 2
    valid_moves = []

    def __init__(self, Location, Owner, Point_Value, Piece_Type):
        y = 0
        if Owner.color == "white":
            y = 1
        else:
            y = -1
        self.valid_moves.extend(vector.Vector(-1, y), vector.Vector(1, y), vector.Vector(0, y))
        super().__init__(Location, Owner, Point_Value, Piece_Type, self.valid_moves, Owner.color)       

    def promote(self):
        pass

    def move(self):
        if self.has_moved == False:
            self.has_moved = True
        super().move()
        self.num_movable_squares= 1
