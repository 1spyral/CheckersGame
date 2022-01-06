import pygame
from src.tools.palette import color

# Mouse class that will be rendered on the screen
class Mouse:
    def __init__(self):
        self.x, self.y = 0, 0
        self.hitbox = (10, 10)
        self.rect = pygame.Rect((self.x, self.y), self.hitbox)
        self.Lclick, self.Rclick = False, False

    # Position of the mouse
    @property
    def pos(self) -> tuple((int, int)):
        return (self.x, self.y)

    # Update position of mouse to match with system cursor
    def update(self) -> None:
        # Update mouse position
        self.x, self.y = pygame.mouse.get_pos()

        mclick: tuple[bool, bool, bool] = pygame.mouse.get_pressed()
        self.Lclick: bool = mclick[0]
        self.Rclick: bool = mclick[2]
        self.rect.x, self.rect.y = self.x, self.y

    # Draw mouse on screen
    def render(self, screen: pygame.Surface) -> None:
        # Mouse is a small square
        pygame.draw.rect(screen, color["red"], self.rect) 

# Initialize cursor
cursor = Mouse()
