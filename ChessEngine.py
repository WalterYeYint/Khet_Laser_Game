class GameState():
    def __init__(self, piece_positions, DIMENSION_X, DIMENSION_Y):
        self.board = [["----" for i in range(DIMENSION_X)] for j in range(DIMENSION_Y)]
        for i in piece_positions:
            self.board[i.position[0]][i.position[1]] = i.text
        self.eyes = []

        # self.board = [
        #     ["rS", "--", "--", "--", "rA", "rP", "rA", "rY", "--", "--"],
        #     ["--", "--", "rY", "--", "--", "--", "--", "--", "--", "--"],
        #     ["--", "--", "--", "sY", "--", "--", "--", "--", "--", "--"],
        #     ["rY", "--", "sY", "--", "rC", "rC", "--", "rY", "--", "sY"],
        #     ["rY", "--", "sY", "--", "sC", "sC", "--", "rY", "--", "sY"],
        #     ["--", "--", "--", "--", "--", "--", "rY", "--", "--", "--"],
        #     ["--", "--", "--", "--", "--", "--", "--", "sY", "--", "--"],
        #     ["--", "--", "sY", "sA", "sP", "sA", "--", "--", "--", "sS"]
        # ]

        self.silverToMove = True
        self.laser_status = False
        self.moveLog = []
    
    def makeMove(self, move, piece):
        src_pt = [move.startRow, move.startCol]
        dest_t = [move.endRow + 1, move.endCol]
        dest_b = [move.endRow - 1, move.endCol]
        dest_l = [move.endRow, move.endCol + 1]
        dest_r = [move.endRow, move.endCol - 1]
        dest_tl = [move.endRow + 1, move.endCol + 1]
        dest_bl = [move.endRow - 1, move.endCol + 1]
        dest_br = [move.endRow - 1, move.endCol - 1]
        dest_tr = [move.endRow + 1, move.endCol - 1]
        # print(src_pt, dest_t, dest_b, dest_l, dest_r, dest_tl, dest_bl, dest_br, dest_tr)
        if src_pt == dest_t or src_pt == dest_b or src_pt == dest_l or src_pt == dest_r \
            or src_pt == dest_bl or src_pt == dest_br \
                or src_pt == dest_tl or src_pt == dest_tr:
            if self.board[move.startRow][move.startCol][3:4] == "C":
                if self.board[move.endRow][move.endCol][3:4] == "Y" or self.board[move.endRow][move.endCol][3:4] == "A" or self.board[move.endRow][move.endCol][3:4] == "-":
                    self.board[move.startRow][move.startCol] = move.pieceCaptured
                    self.board[move.endRow][move.endCol] = move.pieceMoved
                    piece.position = [move.endRow, move.endCol]
                    self.moveLog.append(move)
                    self.silverToMove = not self.silverToMove
                    self.laser_status = True
                else:
                    print("This piece cannot be swapped")
            elif self.board[move.endRow][move.endCol] == "----":
                self.board[move.startRow][move.startCol] = "----"
                self.board[move.endRow][move.endCol] = move.pieceMoved
                piece.position = [move.endRow, move.endCol]
                self.moveLog.append(move)
                self.silverToMove = not self.silverToMove
                self.laser_status = True
            else:
                print("This place is occupied")
        else:
            print("Pieces can only be moved 1 square")


class Move():

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

class Piece:
    def __init__(self, position, color, id, name):
        self.position = position
        self.color = color
        self.id = id
        self.name = name
class Sphinx(Piece):
    def __init__(self, position, color, id, name, orientation):
        Piece.__init__(self, position, color, id, name)
        self.orientation = orientation
        self.text = "{}{}S".format(self.id, self.color)

class Pharoh(Piece):
    def __init__(self, position, color, id, name, orientation):
        Piece.__init__(self, position, color, id, name)
        self.orientation = orientation
        self.text = "{}{}P".format(self.id, self.color)

class Anubis(Piece):
    def __init__(self, position, color, id, name, orientation):
        Piece.__init__(self, position, color, id, name)
        self.orientation = orientation
        self.shield = None
        self.text = "{}{}A".format(self.id, self.color)

class Pyramid(Piece):
    def __init__(self, position, color, id, name, orientation):
        Piece.__init__(self, position, color, id, name)
        self.orientation = orientation
        self.mirror = None
        self.text = "{}{}Y".format(self.id, self.color)

class Scarab(Piece):
    def __init__(self, position, color, id, name, orientation):
        Piece.__init__(self, position, color, id, name)
        self.orientation = orientation
        self.mirror = None
        self.text = "{}{}C".format(self.id, self.color)