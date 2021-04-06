class GameState():
    def __init__(self):
        self.board = [
            ["rS", "--", "--", "--", "rA", "rP", "rA", "rY", "--", "--"],
            ["--", "--", "rY", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "sY", "--", "--", "--", "--", "--", "--"],
            ["rY", "--", "sY", "--", "rC", "rC", "--", "rY", "--", "sY"],
            ["rY", "--", "sY", "--", "sC", "sC", "--", "rY", "--", "sY"],
            ["--", "--", "--", "--", "--", "--", "rY", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "sY", "--", "--"],
            ["--", "--", "sY", "sA", "sP", "sA", "--", "--", "--", "sS"]
        ]

        self.silverToMove = True
        self.moveLog = []
    
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
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

