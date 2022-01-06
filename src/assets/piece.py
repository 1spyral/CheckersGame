import pygame
from src.tools.palette import color
from src.tools.crown import crown


# Class for player pieces on the board
class Piece():
    def __init__(self, row: int, col: int, pieceColor: str):
        self.row = row
        self.col = col
        # Which side the piece will be on
        self.color = pieceColor
        # A piece never starts as a king
        self.king = False
        # X and Y coordinates will be calculated in calc_pos()
        self.x = 0
        self.y = 0
        # Calculates XY coordinates
        self.calc_pos()

    # Determines the rendering position of the piece
    def calc_pos(self) -> None:
        self.x = 100 * self.col + 50
        self.y = 100 * self.row + 50
    
    # Draws the piece out on the board
    def render(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, color[self.color], (self.x, self.y), 25)
        # Blit king's crown if the piece is a king
        if self.king:
            screen.blit(crown, (self.x - crown.get_width()//2, self.y - crown.get_height()//2))

    # Method to change position of piece
    def move(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        # Calculate new XY coordinates of the piece
        self.calc_pos()
