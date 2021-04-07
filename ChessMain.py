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
def loadImages(Piece_List):
    pieces = []
    for i in Piece_List:
        pieces.append(i.text[2:4])
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

#######################################
# MAIN DRIVER. THIS WILL HANDLE USER INPUT AND UPDATING GRAPHICS

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, 8 * SQ_SIZE))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    red_Sphinx = ChessEngine.Sphinx([0, 0], "r", "01", 180)
    silver_Sphinx = ChessEngine.Sphinx([7, 9], "s", "02", 0)
    red_Pharoh = ChessEngine.Pharoh([0, 5], "r", "01", 180)
    silver_Pharoh = ChessEngine.Pharoh([7, 4], "s", "02", 0)
    red_Anubis_1 = ChessEngine.Anubis([0, 4], "r", "01", 180)
    red_Anubis_2 = ChessEngine.Anubis([0, 6], "r", "02", 180)
    silver_Anubis_1 = ChessEngine.Anubis([7, 3], "s", "03", 0)
    silver_Anubis_2 = ChessEngine.Anubis([7, 5], "s", "04", 0)
    red_Scarab_1 = ChessEngine.Scarab([3, 4], "r", "01", 0)
    red_Scarab_2 = ChessEngine.Scarab([3, 5], "r", "02", 90)
    silver_Scarab_1 = ChessEngine.Scarab([4, 4], "s", "03", -90)
    silver_Scarab_2 = ChessEngine.Scarab([4, 5], "s", "04", 180)
    red_Pyramid_1 = ChessEngine.Pyramid([0, 7], "r", "01", -90)
    red_Pyramid_2 = ChessEngine.Pyramid([1, 2], "r", "02", 0)
    red_Pyramid_3 = ChessEngine.Pyramid([3, 0], "r", "03", 180)
    red_Pyramid_4 = ChessEngine.Pyramid([3, 7], "r", "04", -90)
    red_Pyramid_5 = ChessEngine.Pyramid([4, 0], "r", "05", -90)
    red_Pyramid_6 = ChessEngine.Pyramid([4, 7], "r", "06", 180)
    red_Pyramid_7 = ChessEngine.Pyramid([5, 6], "r", "07", -90)
    silver_Pyramid_1 = ChessEngine.Pyramid([2, 3], "s", "08", 90)
    silver_Pyramid_2 = ChessEngine.Pyramid([3, 2], "s", "09", 0)
    silver_Pyramid_3 = ChessEngine.Pyramid([3, 9], "s", "10", 90)
    silver_Pyramid_4 = ChessEngine.Pyramid([4, 2], "s", "11", 90)
    silver_Pyramid_5 = ChessEngine.Pyramid([4, 9], "s", "12", 0)
    silver_Pyramid_6 = ChessEngine.Pyramid([6, 7], "s", "13", 180)
    silver_Pyramid_7 = ChessEngine.Pyramid([7, 2], "s", "14", 90)
    # Piece_List = [red_Sphinx, silver_Sphinx, red_Pyramid_1, silver_Pyramid_1]
    Piece_List = [red_Sphinx, silver_Sphinx, red_Pharoh, silver_Pharoh, red_Anubis_1,\
        red_Anubis_2, silver_Anubis_1, silver_Anubis_2, red_Scarab_1, red_Scarab_2, silver_Scarab_1,\
            silver_Scarab_2, red_Pyramid_1, red_Pyramid_2, red_Pyramid_3, red_Pyramid_4, red_Pyramid_5,\
                red_Pyramid_6, red_Pyramid_7, silver_Pyramid_1, silver_Pyramid_2, silver_Pyramid_3, silver_Pyramid_4,\
                    silver_Pyramid_5, silver_Pyramid_6, silver_Pyramid_7]

    gs = ChessEngine.GameState(Piece_List)
    loadImages(Piece_List)
    print(IMAGES)
    running = True
    sqSelected = ()
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
    #         elif e.type == p.MOUSEBUTTONDOWN:
    #             location = p.mouse.get_pos()
    #             col = location[0] // SQ_SIZE
    #             row = location[1] // SQ_SIZE
    #             if sqSelected == (row, col):
    #                 sqSelected = ()
    #                 playerClicks = []
    #             else:
    #                 sqSelected = (row, col)
    #                 playerClicks.append(sqSelected)
    #             if len(playerClicks) == 2:
    #                 if gs.board[playerClicks[0][0]][playerClicks[0][1]] == "--":
    #                     sqSelected = ()
    #                     playerClicks = []
    #                 else:
    #                     move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
    #                     print(move.getChessPosition())
    #                     gs.makeMove(move)
    #                     sqSelected = ()
    #                     playerClicks = []
    #                     # print(gs.board)

        drawGameState(screen, gs, Piece_List)
        clock.tick(MAX_FPS)
        p.display.flip()
##################################################
# Responsible for all graphics in a current game state

def drawGameState(screen, gs, Piece_List):
    drawBoard(screen)
    drawPieces(screen, gs.board, Piece_List)

##################################################
# Draw the squares on the board.

def drawBoard(screen):
    # colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION_Y):
        for c in range(DIMENSION_X):
            # color = colors[((r+c) % 2)]
            p.draw.rect(screen, p.Color("gray"), p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE), 5)

def drawPieces(screen, board, Piece_List):
    for r in range(DIMENSION_Y):
        for c in range(DIMENSION_X):
            piece = board[r][c]
            if piece != "----":
                for i in Piece_List:
                    if piece == i.text:
                        screen.blit(p.transform.rotate(IMAGES[piece[2:4]], i.orientation), p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            # else:
            #     screen.blit(IMAGES["--"],p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                

if __name__ == "__main__":
    main()
