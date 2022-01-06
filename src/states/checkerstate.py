import pygame
from src.tools.palette import color
from src.assets.board import Board
from src.tools.button import Button
from src.tools.font import font


# State where the checker game is run
class CheckerState():

    # Button to return to menu after game ends
    menu = Button((225, 500), (350, 200))

    def __init__(self):
        self.change = None
        self.menu.function = self.menuButton
        self.menuText = font.render(str("Main Menu"), True, color["black"])
    
    # Function to return to main menu
    def menuButton(self) -> None:
        self.change = "menu"
        pygame.time.delay(500)

    # Runs when entering state, initializes game
    def setup(self) -> None:
        # Attribute determines whether the game has ended or not
        self.end = False
        # The colour of the winner, None at the beginning
        self.winner = None
        # Creates a board from the Board class
        self.board = Board()
        self.winText = None
        # The piece that is selected by the player
        self.active = None 
        # Black goes first in checkers, unlike chess :)
        self.turn = "black"
        # Possible moves for the active piece, none since no active piece on setup
        self.moves = []

    # Used to update the state
    def update(self) -> None:
        # Normal code that is run
        if not self.end:
            # Checks if a tile or piece is being selected
            if pygame.mouse.get_pressed()[0]:
                self.activate(pygame.mouse.get_pos()[1] // 100, pygame.mouse.get_pos()[0] // 100)
            # Checks if there is a winner
            if self.board.end():
                # Ends game and releases winner
                self.end = True
                self.winner = self.board.end()
                # Initializes ending text
                self.winText = font.render(self.winner + " wins!", True, color["black"])
        # Code that is run if the game ended
        else:
            self.menu.update()

    # Draws the game out
    def render(self, screen: pygame.Surface) -> None:
        # Renders board
        self.board.render(screen)
        # Renders valid moves
        for move in self.moves:
            pygame.draw.circle(screen, color["blue"], (move[1] * 100 + 50, move[0] * 100 + 50), 15)
        # Draws ending screen, if game is over
        if self.end:
            self.menu.render(screen)
            screen.blit(self.menuText, (250, 545))
            pygame.draw.rect(screen, color["blue"], pygame.Rect((200, 250), (400, 200)))
            screen.blit(self.winText, (250, 300))

    # Select a piece or tile
    def activate(self, row: int, col: int) -> bool:
        # Checks if a valid piece is selected
        if self.active:
            # Checks if piece can move to desired location
            # Moves if boolean returns True
            if not self.move(row, col):
                self.active = None
                self.activate(row, col)
        # Activates a piece
        piece = self.board.board[row][col]
        if piece and piece.color == self.turn:
            self.active = piece
            # Calculates possible moves for that piece
            self.moves = self.board.valid_moves(piece)
            # Returns true meaning that a piece was activated
            return True

        # Returns false meaning that a new piece was not activated
        return False

    # Executed when a piece is moved
    def move(self, row: int, col: int) -> bool:
        # Piece that will be moved
        piece = self.board.board[row][col]
        if self.active and not piece and (row, col) in self.moves:
            # Moves the piece
            self.board.move(self.active, row, col)
            skipped = self.moves[(row, col)]
            # Checks if piece skipped (ate) any enemy pieces
            if skipped:
                # Deletes those skipped pieces
                self.board.skip(skipped)
            # Changes turn to other player
            if self.turn == "white":
                self.turn = "black"
            elif self.turn == "black":
                self.turn = "white"
            # Resets valid moves
            self.moves = []
        # If function fails
        else:
            return False
        # If function succeeds
        return True

