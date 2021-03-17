import re

def print_board(board):
    """This function prints out the state of the board."""

    output = "     a     b     c     d     e     f     g     h\n"   # Horizontal coordinates
    for column in range(len(board)):
        output += "  " + ("+-----" * len(board)) + "+\n" # Print the top border of a cell.
        output += "  " + (("|" + (" " * 5)) * len(board)) + "|\n" + str(column+1) + " " # Print a blank line in a cell and add is vertical coord

        # For each square in the board.
        for row in range(len(board)):
            piece_representation = None
            if(board[column][row] != None):
                pass # TODO: When pieces are implemented print their identifier.
            else:
                piece_representation = " "
            output += ("|  " + piece_representation + "  ")

        output += "|\n  " + ((("|" + (" " * 5)) * len(board)) + "|\n")  # Another blank line in a cell
    output += "  "+  ("+-----" * len(board)) + "+\n" # Print the bottom border of the board
    print(output)


def parse_input(user_input):
    str_coords = re.findall('[a-h][1-8]', user_input.lower())
    coords = []
    for coord in str_coords:
        x = user_input[0]
        y = user_input[1]
        letter = x

        if (x == "a"):
            x = 1
        elif (x == "b"):
            x = 2
        elif (x == "c"):
            x = 3
        elif (x == "d"):
            x = 4
        elif (x == "e"):
            x = 5
        elif (x == "f"):
            x = 6
        elif (x == "g"):
            x = 7
        else:
            x = 8
        coords.append(Coordinate(x - 1 , y - 1, letter))
    return coords

def test_io_manager():
    # Nested list comprehension that creates an 8x8 two dimensional list populated by None.
    board = [[None for i in range(8)] for i in range(8)]
    print_board(board)
    user_input = input("Please enter the coordinates of the piece you want to move, and where you want to move it to. Example Input: a1 to a7.\n")
    print(parse_input(user_input))