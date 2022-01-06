import pygame
from src.tools.button import Button
from src.tools.palette import color
from src.tools.font import font
import sys

# Button to start the checker game
checker = Button((100, 200), (600, 200))
# Button to quit the program
quit = Button((100, 500), (600, 200))


# Main menu state, prior to starting the game
class MenuState():
    def __init__(self):
        self.change = None
        # Initializes button text
        self.checkerText = font.render(str("play"), True, color["black"])
        self.quitText = font.render(str("quit"), True, color["black"])
        self.titleText = font.render(str("Checkers"), True, color["black"])

    # Function to set up the state when entering it
    def setup(self) -> None:
        # Enters the checker game
        def checkerButton():
            self.change = "checker"
        # Quits the program
        def quitButton():
            pygame.quit()
            sys.exit()

        # Assigns functions to buttons
        checker.function = checkerButton
        quit.function = quitButton

    # Function to update the state
    def update(self) -> None:
        # Updates buttons
        checker.update()
        quit.update()

    # Draws the menu state out
    def render(self, screen: pygame.Surface) -> None:
        # Renders buttons
        checker.render(screen)
        quit.render(screen)
        # Renders text
        screen.blit(self.checkerText, (340, 250))
        screen.blit(self.quitText, (340, 550))
        screen.blit(self.titleText, (280, 70))