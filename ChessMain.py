import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION_X = 10
DIMENSION_Y = 8
SQ_SIZE = WIDTH // DIMENSION_X
MAX_FPS = 15
IMAGES = {}

###################################
# LOAD THE IMAGES
def loadImages():
    pieces = ["rS", "rC", "rP", "rA", "rY", "sS", "sC", "sP", "sA", "sY", "--"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

#######################################
# MAIN DRIVER. THIS WILL HANDLE USER INPUT AND UPDATING GRAPHICS

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, 8 * SQ_SIZE))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    # print(IMAGES)
    running = True
    sqSelected = ()
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    if gs.board[playerClicks[0][0]][playerClicks[0][1]] == "--":
                        sqSelected = ()
                        playerClicks = []
                    else:
                        move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        print(move.getChessPosition())
                        gs.makeMove(move)
                        sqSelected = ()
                        playerClicks = []
                        # print(gs.board)

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
##################################################
# Responsible for all graphics in a current game state

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

##################################################
# Draw the squares on the board.

def drawBoard(screen):
    # colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION_Y):
        for c in range(DIMENSION_X):
            # color = colors[((r+c) % 2)]
            p.draw.rect(screen, p.Color("gray"), p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE), 5)

def drawPieces(screen, board):
    for r in range(DIMENSION_Y):
        for c in range(DIMENSION_X):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            else:
                screen.blit(IMAGES["--"],p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                

if __name__ == "__main__":
    main()
