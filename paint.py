import pygame
import math

pygame.init()

screen = pygame.display.set_mode([500, 500])

points = [[]]
brush_sizes = [3]
brush_color = (0,0,0)

class Shape:
    def display(self, pos, scale, color):
        pass

class Plus(Shape):
    def display(self, pos, scale, color):
        pygame.draw.rect(screen, color, pygame.Rect(float(pos.x + 5 * scale - scale/2), float(pos.y), float(scale), float(scale * 10)))
        pygame.draw.rect(screen, color, pygame.Rect(float(pos.x), float(pos.y + 5 * scale - scale/2), float(scale * 10), float(scale)))

class Minus(Shape):
    def display(self, pos, scale, color):
        pygame.draw.rect(screen, color, pygame.Rect(float(pos.x), float(pos.y + 5 * scale - scale/2), float(scale * 10), float(scale)))


class Button:

    # pos is Vector2, scale is float, shape is Shape object, color is pygame color, hitbox is Vector2
    def __init__(self, pos, scale, shape, color, hitbox):
        self.pos = pos
        self.scale = scale
        self.shape = shape
        self.color = color
        self.hitbox = hitbox
    
    def display(self):
        self.shape.display(self.pos, self.scale, self.color)

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

# credit to Davis Yoshida (Stack Overflow)
def map_range(value, start1, stop1, start2, stop2):
   return (value - start1) / (stop1 - start1) * (stop2 - start2) + start2

# Buttons
plus_button = Button(pygame.Vector2(10, 10), 3, Plus(), (0,0,0), pygame.Vector2(30,30))
minus_button = Button(pygame.Vector2(45, 10), 3, Minus(), (0,0,0), pygame.Vector2(30, 30))


running = True
while running:

    # let user quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if plus_button.mouse_over():
                brush_sizes[-1] += 1
            if minus_button.mouse_over():
                brush_sizes[-1] -= 1

    # easy to use variables
    width = pygame.display.get_surface().get_width()
    height = pygame.display.get_surface().get_height()
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    # background
    screen.fill((255, 255, 255))

    # get user input
    mousePos = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[1] > 50:
        points[-1].append(mousePos)
    elif points[-1] != []:
        points.append([])
        brush_sizes.append(brush_sizes[-1])


    # display brushstrokes
    for pointlist, brush_size in zip(points, brush_sizes):
         for point1, point2 in zip(pointlist, pointlist[1:]):
             dist = point1.distance_to(point2)
             for i in range(0, int(dist)):
                pos = pygame.Vector2(map_range(i, 0, dist, point1.x, point2.x), map_range(i, 0, dist, point1.y, point2.y))
                pygame.draw.circle(screen, (0,0,0), pos, brush_size)

    #display button tray
    pygame.draw.rect(screen, (200,200,200), pygame.Rect(0, 0, width, 50))
    plus_button.display()
    minus_button.display()

    #display mouse brush
    pygame.draw.circle(screen, (0,0,0), mousePos, brush_sizes[-1])
    
    # Flip the display
    pygame.display.flip()


pygame.quit()