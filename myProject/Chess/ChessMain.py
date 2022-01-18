"""
This is our main driver file.
It will be responsible for user input as well as displaying the game. GameState object
"""
import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Initialize the images for each piece as a global dictionary
'''


def loadImages():
    pieces = ['bp', 'bR', 'bN', 'bB', 'bK', 'bQ', 'wp', 'wR', 'wN', 'wB', 'wK', 'wQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    sqSelected = () # this tuple keep track of the selected square as (row, col)
    playerClicks = [] # keep track of player clicks as row and column as an array.
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # this keeps track of the location of the mouse in the x and y plane
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row,col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


"""
The following methods are responsible for all the graphics
"""


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


"""
Draw the squares on our display
"""


def drawBoard(screen):
    colours = [p.Color(235, 235, 208), p.Color(119, 148, 85)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            colour = colours[((r + c) % 2)]
            p.draw.rect(screen, colour, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
Draw the Pieces on the Board. 
"""


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == '__main__':
    main()
