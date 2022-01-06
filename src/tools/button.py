import pygame
from src.tools.mouse import cursor
from src.tools.palette import color

# Class used to make simple buttons
class Button:
    def __init__(self, position: tuple((int, int)), dimensions: tuple((int, int)), function = None):
    
        self.dims = dimensions
        self.pos = position

        self.rect = pygame.Rect(self.pos, self.dims)

        self.color = (30, 30, 35)
        self.offHover = color["yellow"]
        self.onHover = color["white"]

        # Function that runs when button is clicked
        self.function = function
    
    # Change the colouring of the button, optional
    def setColor(self, offHover=None, onHover=None) -> None:
        self.offHover = offHover if offHover else self.offHover 
        self.onHover = onHover if onHover else self.onHover        

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    @property
    def w(self):
        return self.dims[0]
    
    @property
    def h(self):
        return self.dims[1]

    # Update the button's properties
    def update(self) -> None:
        # Change colour of button if mouse is over it
        self.color = self.offHover
        if cursor.rect.colliderect(self.rect):
            self.color = self.onHover
            # Determines whether or not the button is clicked
            if cursor.Lclick:
                # Runs button function
                self.function()
    
    # Draw the button on the screen
    def render(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, self.rect)

    # Dunder method, str(Button()) will give you some information on it
    def __str__(self) -> str:
        return f"Button({self.dims}, {self.pos}, self.function)"
