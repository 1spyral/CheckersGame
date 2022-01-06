from typing import Container, Set
import pygame
from src.assets.piece import Piece
from src.tools.palette import color


# Main board class
class Board:
    def __init__(self):
        self.board = []
        # Initialize piece count of each team
        self.black_lives = 12
        self.white_lives = 12
        for row in range(8):
            self.board.append([])
            for col in range(8):
                if col % 2 == ((row +  1) % 2):
                    # Initialize white pieces
                    if row < 3:
                        self.board[row].append(Piece(row, col, "white"))
                    elif row > 4:
                    # Initialize black pieces
                        self.board[row].append(Piece(row, col, "black"))
                    else:
                        self.board[row].append(None)
                else:
                    self.board[row].append(None)
    

    def render(self, screen: pygame.Surface) -> None:
        # Draws tiles
        for row in range(8):
            for col in range(row % 2, 8, 2):
                pygame.draw.rect(screen, color["bgGreen"], (row * 100, col * 100, 100, 100))
        # Draws pieces
        for row in range(8):
            for col in range(8):
                if self.board[row][col]:
                    self.board[row][col].render(screen)

    # Board function for moving a piece
    def move(self, piece: Piece, row: int, col: int) -> None:
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        # Checks if piece becomes a king
        if row == 7 or row == 0:
            piece.king = True

    # Function for skipping (eating) pieces
    def skip(self, pieces: set) -> None:
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece:
                # Determines if piece eaten was black or white
                if piece.color == "black":
                    self.black_lives -= 1
                else:
                    self.white_lives -= 1
    
    # Checks if any team loses
    def end(self) -> str:
        if self.black_lives <= 0:
            # White wins
            return "white"
        elif self.white_lives <= 0:
            # Black wins
            return "black"
        # Fall-back return operator, this code should not run
        return None 
    
    # Function to find what moves are valid for a piece
    def valid_moves(self, piece: Piece) -> set:
        # The set that will contain valid moves
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        # Checks for valid moves above the piece
        if piece.color == "black" or piece.king:
            moves.update(self.traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self.traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        # Checks for valid moves below the piece
        if piece.color == "white" or piece.king:
            moves.update(self.traverse_left(row +1, min(row+3, 8), 1, piece.color, left))
            moves.update(self.traverse_right(row +1, min(row+3, 8), 1, piece.color, right))

        return moves

    # Function to check possible moves left of the piece
    def traverse_left(self, start: int, stop: int, step: int, color: str, left: int, skipped: list = []) -> set:
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            # The tile being checked
            current = self.board[r][left]
            # Check if the tile is occupied
            if not current:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                # Check if more pieces can be skipped (jumped)
                # In standard checkers, up to two pieces can be skipped at a time
                if last:
                    # Checks whether you are skipping upwards
                    if step == -1:
                        row = max(r-3, 0)
                    # Or downwards
                    else:
                        row = min(r+3, 8)
                    # Checks in either direction for more skips
                    moves.update(self.traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self.traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            # End loop, since own colour can not be skipped
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    # Function to check possible moves right of the piece
    def traverse_right(self, start: int, stop: int, step: int, color: str, right: int, skipped: list = []) -> set:
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= 8:
                break

            # The tile being checked
            current = self.board[r][right]
            # Check if the tile is occupied
            if not current:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                # Check if more pieces can be skipped (jumped)
                # In standard checkers, up to two pieces can be skipped at a time
                if last:
                    # Checks whether you are skipping upwards
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, 8)
                    # Checks in either direction for more skips
                    moves.update(self.traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self.traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            # End loop, since own colour can not be skipped
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves
