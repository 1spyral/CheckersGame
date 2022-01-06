# Zhan, Luke
# Zhang, Samuel
# ICS2O1 Final Project
# Checkers Game

import pygame
from pygame import mixer
from src.states import *
from src.tools.mouse import cursor
from src.tools.palette import color
from statemachine import StateMachine

# Pygame background music player
mixer.init()
mixer.music.load("src/tools/checkersmusic.mp3")
mixer.music.set_volume(0.3)
mixer.music.play()

# Updates the game
def update():
    # Update the location of cursor
    cursor.update()
    # Tells StateMachine to update
    state.update()
    # Update display here
    win.fill(color["beige"])
    state.render(win)
    cursor.render(win)
    pygame.display.update()


# Main process of the code
if __name__ == "__main__":
    # Initialize pygame
    pygame.init()

    # Constant used for window size
    WIDTH, HEIGHT = 800, 800

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    # Set window name
    pygame.display.set_caption("Checkers")
    # Custom mouse is used, make default invisible
    pygame.mouse.set_visible(False)

    # Initialize StateMachine
    state = StateMachine()

    # Main game loop
    run = True
    while run:
        # Checks if game quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Updates mouse, state, renders things
        update()
        
        # Small 10 millisecond delay
        pygame.time.delay(10)
    
    # End the process
    pygame.quit()
