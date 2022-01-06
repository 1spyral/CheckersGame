import pygame
from src.states import *


# Class for the state machine, which handles changing of game states
class StateMachine:
  
    def __init__(self):
        # List of states used in the game
        self.states = {
            "menu": menustate.MenuState(),
            "checker": checkerstate.CheckerState()
        }
        # The initial state will be the main menu
        self.currentstate = self.states["menu"]
        self.currentstate.setup()
  
    # Function to change between states
    def change(self, nxt: str) -> None:
        self.currentstate.change = None
        # Picks new state from the self.states dictionary
        self.currentstate = self.states[nxt]
        # Commences state setup
        self.currentstate.setup()
  
    # Update the current state
    def update(self) -> None:
        self.currentstate.update()
        # Checks if state will be changed
        if self.currentstate.change:
            # Switches to new state
            self.change(self.currentstate.change)
            
    # Draws the state out
    def render(self, screen: pygame.Surface) -> None:
        self.currentstate.render(screen)
