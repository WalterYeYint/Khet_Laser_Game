#!/usr/bin/env python3

import pygame as p
import ChessEngine
import time

WIDTH = HEIGHT = 800
DIMENSION_X = 10
DIMENSION_Y = 8
SQ_SIZE = WIDTH // DIMENSION_X
MAX_FPS = 15
IMAGES = {}

red_Sphinx = ChessEngine.Sphinx([0, 0], "r", "01", "Sphinx", 180)
silver_Sphinx = ChessEngine.Sphinx([7, 9], "s", "02", "Sphinx", 0)
red_Pharoh = ChessEngine.Pharoh([0, 5], "r", "01", "Pharoh", 180)
silver_Pharoh = ChessEngine.Pharoh([7, 4], "s", "02", "Pharoh", 0)
red_Anubis_1 = ChessEngine.Anubis([0, 4], "r", "01", "Anubis", 180)
red_Anubis_2 = ChessEngine.Anubis([0, 6], "r", "02", "Anubis", 180)
silver_Anubis_1 = ChessEngine.Anubis([7, 3], "s", "03", "Anubis", 0)
silver_Anubis_2 = ChessEngine.Anubis([7, 5], "s", "04", "Anubis", 0)
red_Scarab_1 = ChessEngine.Scarab([3, 4], "r", "01", "Scarab", 0)
red_Scarab_2 = ChessEngine.Scarab([3, 5], "r", "02", "Scarab", -90)
silver_Scarab_1 = ChessEngine.Scarab([4, 4], "s", "03", "Scarab", 90)
silver_Scarab_2 = ChessEngine.Scarab([4, 5], "s", "04", "Scarab", 180)
red_Pyramid_1 = ChessEngine.Pyramid([0, 7], "r", "01", "Pyramid", 90)
red_Pyramid_2 = ChessEngine.Pyramid([1, 2], "r", "02", "Pyramid", 0)
red_Pyramid_3 = ChessEngine.Pyramid([3, 0], "r", "03", "Pyramid", 180)
red_Pyramid_4 = ChessEngine.Pyramid([3, 7], "r", "04", "Pyramid", 90)
red_Pyramid_5 = ChessEngine.Pyramid([4, 0], "r", "05", "Pyramid", 90)
red_Pyramid_6 = ChessEngine.Pyramid([4, 7], "r", "06", "Pyramid", 180)
red_Pyramid_7 = ChessEngine.Pyramid([5, 6], "r", "07", "Pyramid", 90)
silver_Pyramid_1 = ChessEngine.Pyramid([2, 3], "s", "08", "Pyramid", -90)
silver_Pyramid_2 = ChessEngine.Pyramid([3, 2], "s", "09", "Pyramid", 0)
silver_Pyramid_3 = ChessEngine.Pyramid([3, 9], "s", "10", "Pyramid", -90)
silver_Pyramid_4 = ChessEngine.Pyramid([4, 2], "s", "11", "Pyramid", -90)
silver_Pyramid_5 = ChessEngine.Pyramid([4, 9], "s", "12", "Pyramid", 0)
silver_Pyramid_6 = ChessEngine.Pyramid([6, 7], "s", "13", "Pyramid", 180)
silver_Pyramid_7 = ChessEngine.Pyramid([7, 2], "s", "14", "Pyramid", -90)
# Piece_List = [red_Sphinx, silver_Sphinx, red_Pyramid_1, silver_Pyramid_1]
Piece_List = [red_Sphinx, silver_Sphinx, red_Pharoh, silver_Pharoh, red_Anubis_1,\
    red_Anubis_2, silver_Anubis_1, silver_Anubis_2, red_Scarab_1, red_Scarab_2, silver_Scarab_1,\
        silver_Scarab_2, red_Pyramid_1, red_Pyramid_2, red_Pyramid_3, red_Pyramid_4, red_Pyramid_5,\
            red_Pyramid_6, red_Pyramid_7, silver_Pyramid_1, silver_Pyramid_2, silver_Pyramid_3, silver_Pyramid_4,\
                silver_Pyramid_5, silver_Pyramid_6, silver_Pyramid_7]
Anubis_List = [red_Anubis_1, red_Anubis_2, silver_Anubis_1, silver_Anubis_2]
Scarab_List = [red_Scarab_1, red_Scarab_2, silver_Scarab_1, silver_Scarab_2]
Pyramid_List = [red_Pyramid_1, red_Pyramid_2, red_Pyramid_3, red_Pyramid_4, red_Pyramid_5, red_Pyramid_6, red_Pyramid_7, \
    silver_Pyramid_1, silver_Pyramid_2, silver_Pyramid_3, silver_Pyramid_4, silver_Pyramid_5, silver_Pyramid_6, silver_Pyramid_7]

red_Eye = []
for i in range(1, 8):
    red_Eye.append([i, 0])
red_Eye.append([0, 1])

silver_Ankh = []
for i in range(6, -1, -1):
    silver_Ankh.append([i, 9])
silver_Ankh.append([7, 8])


###################################
# LOAD THE IMAGES
def loadImages(Piece_List):
    pieces = []
    for i in Piece_List:
        pieces.append(i.text[2:4])
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Images/" + piece + ".png"), (SQ_SIZE - 2, SQ_SIZE - 2))
    IMAGES["--"] = p.transform.scale(p.image.load("Images/" + "--" + ".png"), (SQ_SIZE - 2, SQ_SIZE - 2))
    IMAGES["rE"] = p.transform.scale(p.image.load("Images/" + "rE" + ".png"), (SQ_SIZE - 2, SQ_SIZE - 2))
    IMAGES["sE"] = p.transform.scale(p.image.load("Images/" + "sE" + ".png"), (SQ_SIZE - 2, SQ_SIZE - 2))

#######################################
# MAIN DRIVER. THIS WILL HANDLE USER INPUT AND UPDATING GRAPHICS

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, 8 * SQ_SIZE))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    gs = ChessEngine.GameState(Piece_List, DIMENSION_X, DIMENSION_Y)
    loadImages(Piece_List)
    # print(IMAGES)
    running = True
    sqSelected = ()
    playerClicks = []
    selected_Square = []
    while running:
        for e in p.event.get():
            stepped_on_eye = False
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
                    selected_Square = [playerClicks[0][0], playerClicks[0][1]]
                    if gs.silverToMove == True:
                        if gs.board[playerClicks[0][0]][playerClicks[0][1]][2:3] == "s":
                            pass
                        else:
                            print("It is silver's turn")
                            sqSelected = ()
                            playerClicks = []
                            continue
                    else:
                        if gs.board[playerClicks[0][0]][playerClicks[0][1]][2:3] == "r":
                            pass
                        else:
                            print("It is red's turn")
                            sqSelected = ()
                            playerClicks = []
                            continue
                if len(playerClicks) == 2:
                    if gs.board[playerClicks[0][0]][playerClicks[0][1]] == "----":
                        sqSelected = ()
                        playerClicks = []
                        selected_Square = []
                    else:
                        # print(playerClicks[0])
                        # print(sqSelected[0])
                        for piece in Piece_List:
                            if piece.position == [playerClicks[0][0], playerClicks[0][1]]:
                                # print(piece.position)
                                if gs.silverToMove == True:
                                    for eye in red_Eye:
                                        if [playerClicks[1][0], playerClicks[1][1]] == eye:
                                            print("Only silver pieces can move here")
                                            stepped_on_eye = True
                                            break
                                    if stepped_on_eye == True:
                                        sqSelected = ()
                                        playerClicks = []
                                        selected_Square = []
                                        break
                                elif gs.silverToMove == False:
                                    for eye in silver_Ankh:
                                        if [playerClicks[1][0], playerClicks[1][1]] == eye:
                                            print("Only red pieces can move here")
                                            stepped_on_eye = True
                                            break
                                    if stepped_on_eye == True:
                                        sqSelected = ()
                                        playerClicks = []
                                        selected_Square = []
                                        break
                                if piece.name == "Sphinx":
                                    print("Sphinx can only be rotated")
                                else:
                                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                                    gs.makeMove(move, piece)
                                print(gs.silverToMove)
                                sqSelected = ()
                                playerClicks = []
                                selected_Square = []
                                # print(gs.board)
                                break
            elif e.type == p.KEYDOWN:
                if len(playerClicks) == 1:
                    for piece in Piece_List:
                        if piece.position == [playerClicks[0][0], playerClicks[0][1]]:
                            if piece.name == "Pharoh":
                                print("Pharoh doesn't need to rotate")
                                break
                            if e.key == p.K_LEFT:
                                if piece.name == "Sphinx" and piece.id == "01" and piece.orientation == 270:
                                    print("Sphinx cannot rotate further")
                                    break
                                elif piece.name == "Sphinx" and piece.id == "02" and piece.orientation == 90:
                                    print("Sphinx cannot rotate further")
                                    break
                                else:
                                    piece.orientation += 90
                                    gs.silverToMove = not gs.silverToMove
                            elif e.key == p.K_RIGHT:
                                if piece.name == "Sphinx" and piece.id == "01" and piece.orientation == 180:
                                    print("Sphinx cannot rotate further")
                                    break
                                elif piece.name == "Sphinx" and piece.id == "02" and piece.orientation == 0:
                                    print("Sphinx cannot rotate further")
                                    break
                                else:
                                    piece.orientation -= 90
                                    gs.silverToMove = not gs.silverToMove
                            else:
                                print("Invalid key input")
                                break
                            if piece.orientation >= 360 or piece.orientation <= -360:
                                piece.orientation = 0
                            print(piece.orientation)
                            gs.laser_status = True
                    sqSelected = ()
                    playerClicks = []
                    selected_Square = []

        drawGameState(screen, gs, Piece_List, selected_Square)
        clock.tick(MAX_FPS)
        if gs.laser_status == True:
            drawGameState(screen, gs, Piece_List, selected_Square)
            shootLaser(screen, gs, Piece_List, red_Sphinx, silver_Sphinx, Anubis_List, Scarab_List, Pyramid_List)
            p.display.flip()
            time.sleep(1)
            gs.laser_status = False
        p.display.flip()

##################################################
# Responsible for all graphics in a current game state

def drawGameState(screen, gs, Piece_List, selected_Square):
    drawBoard(screen, selected_Square)
    drawPieces(screen, gs.board, Piece_List)

##################################################
# Draw the squares on the board.

def drawBoard(screen, selected_Square):
    # colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION_Y):
        for c in range(DIMENSION_X):
            p.draw.rect(screen, p.Color("gray"), p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE), 5)
    if len(selected_Square) != 0:
        p.draw.rect(screen, p.Color("blue"), p.Rect(selected_Square[1]*SQ_SIZE, selected_Square[0]*SQ_SIZE, SQ_SIZE, SQ_SIZE), 5)

def drawPieces(screen, board, Piece_List):
    for r in range(DIMENSION_Y):
        for c in range(DIMENSION_X):
            piece = board[r][c]
            if piece != "----":
                for i in Piece_List:
                    if piece == i.text:
                        screen.blit(p.transform.rotate(IMAGES[piece[2:4]], i.orientation), p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            else:
                screen.blit(IMAGES["--"],p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    for r in range(len(red_Eye)):
        if board[red_Eye[r][0]][red_Eye[r][1]] == "----":
            screen.blit(IMAGES["rE"],p.Rect(red_Eye[r][1]*SQ_SIZE, red_Eye[r][0]*SQ_SIZE, SQ_SIZE, SQ_SIZE))
        if board[silver_Ankh[r][0]][silver_Ankh[r][1]] == "----":
            screen.blit(IMAGES["sE"],p.Rect(silver_Ankh[r][1]*SQ_SIZE, silver_Ankh[r][0]*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def shootLaser(screen, gs, Piece_List, red_Sphinx, silver_Sphinx, Anubis_List, Scarab_List, Pyramid_List):
    if gs.silverToMove == True:
        sphinx_piece = red_Sphinx
        i = 0
        j = 0
        moveLaser(screen, gs.board, Piece_List, sphinx_piece, Anubis_List, Scarab_List, Pyramid_List, i, j)

    elif gs.silverToMove == False:
        sphinx_piece = silver_Sphinx
        i = sphinx_piece.position[0]
        j = sphinx_piece.position[1]
        print(i, j)
        moveLaser(screen, gs.board, Piece_List, sphinx_piece, Anubis_List, Scarab_List, Pyramid_List, i, j)

def moveLaser(screen, board, Piece_List, sphinx_piece, Anubis_List, Scarab_List, Pyramid_List, i, j):
    
    laser_orientation = sphinx_piece.orientation
    laser_endpoint = False
    laser_checkpoint = [None, None]
    switch_i = {
        0: -1,
        180: +1,
        -180: +1,
        -360: -1,
    }
    switch_j = {
        270: +1,
        90: -1,
        -90: +1,
        -270: -1,
    }
    while -1 < i < DIMENSION_Y and -1 < j < DIMENSION_X:
        while True:
            if laser_orientation == 180 or laser_orientation == 0 or laser_orientation == -180:
                i += switch_i.get(laser_orientation)
            else:
                j += switch_j.get(laser_orientation)
            print(i, j, DIMENSION_Y)
            if i <= DIMENSION_Y - 1 or j <= DIMENSION_X - 1:
                p.draw.rect(screen, p.Color("red"), p.Rect(j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE), 5)
            if not (-1 < i < DIMENSION_Y and -1 < j < DIMENSION_X and board[i][j] == "----"):
                break
        if i >= DIMENSION_Y:
            i = 7
        elif i <= 0:
            i = 0
        if j >= DIMENSION_X:
            j = 9
        elif j <= 0:
            j = 0
        # print(board[i][j][2:4], Piece_List[2].orientation)
        if board[i][j][3:4] == "A":
            for piece in Anubis_List:
                if piece.id == board[i][j][0:2]:
                    orientation_result = abs(piece.orientation - laser_orientation)
                    if orientation_result == 180:
                        laser_endpoint = True
                        break
                    else:
                        board[i][j] = "----"
                        laser_endpoint = True
                        break
        elif board[i][j][3:4] == "Y":
            for piece in Pyramid_List:
                if piece.id == board[i][j][0:2]:
                    if laser_checkpoint == piece.position:
                        laser_endpoint = True
                        break
                    orientation_result = laser_orientation - piece.orientation
                    print(laser_orientation, piece.orientation, orientation_result)
                    if orientation_result == 0 or orientation_result == 360:
                        laser_orientation += 90
                        laser_checkpoint = piece.position
                        break
                    elif orientation_result == -90 or orientation_result == 270:
                        laser_orientation -= 90
                        laser_checkpoint = piece.position
                        break
                    else:
                        board[i][j] = "----"
                        laser_endpoint = True
                        break
            laser_orientation = checkLaserOrientation(laser_orientation)
        elif board[i][j][3:4] == "C":
            for piece in Scarab_List:
                if piece.id == board[i][j][0:2]:
                    if laser_checkpoint == piece.position:
                        laser_endpoint = True
                        break
                    orientation_result = laser_orientation - piece.orientation
                    print(laser_orientation, piece.orientation, orientation_result)
                    if orientation_result == 0 or orientation_result == 360 or orientation_result == 180 or orientation_result == -180:
                        laser_orientation += 90
                        laser_checkpoint = piece.position
                        break
                    else:
                        laser_orientation -= 90
                        laser_checkpoint = piece.position
                        break
            laser_orientation = checkLaserOrientation(laser_orientation)
        elif board[i][j][3:4] == "P":
            print("You've won")
            break
        elif board[i][j][3:4] == "S":
            break
        elif board[i][j] == "----":
            break
        
        if laser_endpoint == True:
            break

def checkLaserOrientation(laser_orientation):
    if laser_orientation >= 360:
        laser_orientation = laser_orientation - 360
    elif laser_orientation <= -360:
        laser_orientation = laser_orientation + 360
    return laser_orientation

if __name__ == "__main__":
    main()
