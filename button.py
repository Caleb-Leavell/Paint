import pygame
import shape

class Button:

    # pos is Vector2, scale is float, shape is Shape object, color is pygame color, hitbox is Vector2
    def __init__(self, pos: pygame.Vector2, scale: int, shape: shape.Shape, color: tuple, hitbox: pygame.Vector2):
        self.pos = pos
        self.scale = scale
        self.shape = shape
        self.color = color
        self.hitbox = hitbox
    
    def display(self, screen):
        self.shape.display(screen, self.pos, self.scale, self.color)

    def mouse_over(self):
        if (
                pygame.mouse.get_pos()[0] > self.pos.x
            and pygame.mouse.get_pos()[0] < self.pos.x + self.hitbox.x 
            and pygame.mouse.get_pos()[1] > self.pos.y
            and pygame.mouse.get_pos()[1] < self.pos.y + self.hitbox.y
        ):
            return True
        else:
            return False