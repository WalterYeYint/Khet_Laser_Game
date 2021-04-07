class GameState():
    def __init__(self, piece_positions):
        self.board = [["----" for i in range(10)] for j in range(8)]
        for i in piece_positions:
            self.board[i.position[0]][i.position[1]] = i.text

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
        self.moveLog = []
    
    def makeMove(self, move, piece):
        self.board[move.startRow][move.startCol] = "----"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        piece.position = [move.endRow, move.endCol]
        self.moveLog.append(move)
        self.silverToMove = not self.silverToMove


class Move():

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessPosition(self):
        return self.endRow, self.endCol

class Piece:
    def __init__(self, position, color, id):
        self.position = position
        self.color = color
        self.id = id
class Sphinx(Piece):
    def __init__(self, position, color, id, orientation):
        Piece.__init__(self, position, color, id)
        self.orientation = orientation
        self.text = "{}{}S".format(self.id, self.color)

class Pharoh(Piece):
    def __init__(self, position, color, id, orientation):
        Piece.__init__(self, position, color, id)
        self.orientation = orientation
        self.text = "{}{}P".format(self.id, self.color)

class Anubis(Piece):
    def __init__(self, position, color, id, orientation):
        Piece.__init__(self, position, color, id)
        self.orientation = orientation
        self.shield = None
        self.text = "{}{}A".format(self.id, self.color)

class Pyramid(Piece):
    def __init__(self, position, color, id, orientation):
        Piece.__init__(self, position, color, id)
        self.orientation = orientation
        self.mirror = None
        self.text = "{}{}Y".format(self.id, self.color)

class Scarab(Piece):
    def __init__(self, position, color, id, orientation):
        Piece.__init__(self, position, color, id)
        self.orientation = orientation
        self.mirror = None
        self.text = "{}{}C".format(self.id, self.color)