import pygame
import pygame.gfxdraw
import copy
from collections import deque

pygame.init()

screen = pygame.display.set_mode([1280, 720])

stroke = {
    'points' : [],
    'brush_size' : 3,
    'brush_color' : (0,0,0)
}

strokes = [copy.deepcopy(stroke)]

undo_stack = deque()

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

class Circle(Shape):
    def display(self, pos, scale, color):
        pygame.gfxdraw.filled_circle(screen, int(pos.x + scale), int(pos.y + scale), scale, color)
        pygame.gfxdraw.aacircle(screen, int(pos.x + scale), int(pos.y + scale), scale, color)

class Arrow_Forward(Shape):
    def display(self, pos, scale, color):
        pygame
        pygame.draw.line(screen, color, pygame.Vector2(pos.x, pos.y + scale / 2), pygame.Vector2(pos.x + scale, pos.y + scale / 2), int(scale / 10))
        pygame.draw.line(screen, color, pygame.Vector2(pos.x + scale / 1.5, pos.y + scale / 5), pygame.Vector2(pos.x + scale, pos.y + scale / 2), int(scale / 10))
        pygame.draw.line(screen, color, pygame.Vector2(pos.x + scale / 1.5, pos.y + (scale - scale / 5)), pygame.Vector2(pos.x + scale, pos.y + scale / 2), int(scale / 10))

class Arrow_Backward(Shape):
    def display(self, pos, scale, color):
        pygame
        pygame.draw.line(screen, color, pygame.Vector2(pos.x, pos.y + scale / 2), pygame.Vector2(pos.x + scale, pos.y + scale / 2), int(scale / 10))
        pygame.draw.line(screen, color, pygame.Vector2(pos.x, pos.y + scale / 2), pygame.Vector2(pos.x + scale - (scale / 1.5), pos.y + scale / 5 ), int(scale / 10))
        pygame.draw.line(screen, color, pygame.Vector2(pos.x, pos.y + scale / 2), pygame.Vector2(pos.x + scale - (scale / 1.5), pos.y + (scale - scale / 5)), int(scale / 10))

class Button:

    # pos is Vector2, scale is float, shape is Shape object, color is pygame color, hitbox is Vector2
    def __init__(self, pos: pygame.Vector2, scale: int, shape: Shape, color: tuple, hitbox: pygame.Vector2):
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
black_button = Button(pygame.Vector2(80, 10), 15, Circle(), (0,0,0), pygame.Vector2(30, 30))
red_button = Button(pygame.Vector2(115, 10), 15, Circle(), (255,0,0), pygame.Vector2(30, 30))
green_button = Button(pygame.Vector2(150, 10), 15, Circle(), (0,255,0), pygame.Vector2(30, 30))
blue_button = Button(pygame.Vector2(185, 10), 15, Circle(), (0,0,255), pygame.Vector2(30, 30))
white_button = Button(pygame.Vector2(220, 10), 15, Circle(), (255,255,255), pygame.Vector2(30, 30))
undo_button = Button(pygame.Vector2(pygame.display.get_surface().get_width() - 85, 10), 20, Arrow_Backward(), (0,0,0), pygame.Vector2(30,30))
redo_button = Button(pygame.Vector2(pygame.display.get_surface().get_width() - 50, 10), 20, Arrow_Forward(), (0,0,0), pygame.Vector2(30,30))



running = True
while running:

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if plus_button.mouse_over():
                stroke['brush_size'] += 1
            if minus_button.mouse_over():
                stroke['brush_size'] -= 1
            if black_button.mouse_over():
                stroke['brush_color'] = (0,0,0)
            if red_button.mouse_over():
                stroke['brush_color'] = (255,0,0)
            if green_button.mouse_over():
                stroke['brush_color'] = (0,255,0)
            if blue_button.mouse_over():
                stroke['brush_color'] = (0,0,255)
            if white_button.mouse_over():
                stroke['brush_color'] = (255,255,255)
            if undo_button.mouse_over():
                if len(strokes) >= 2:
                    undo_stack.append(strokes[-2])
                    del strokes[-2]
            if redo_button.mouse_over():
                if(len(undo_stack) >= 1):
                    strokes.insert(-2, undo_stack.pop())
                
                

    # easy to use variables
    width = pygame.display.get_surface().get_width()
    height = pygame.display.get_surface().get_height()
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    # background
    screen.fill((255, 255, 255))

    # adding positions to brush if mouse held down
    mousePos = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    if pygame.mouse.get_pressed()[0] and mouse_pos.y > 50:
        stroke['points'].append(mouse_pos)
        strokes[-1] = copy.deepcopy(stroke)
    elif len(strokes[-1]['points']) >= 1:
        strokes.append(copy.deepcopy(stroke))
        strokes[-1]['points'] = []
        stroke['points'] = []

    # display brushstrokes
    for curr_stroke in strokes:
        for point1, point2 in zip(curr_stroke['points'], curr_stroke['points'][1:]):
            dist = point1.distance_to(point2)
            for i in range(0, int(dist)):
                pos = pygame.Vector2(map_range(i, 0, dist, point1.x, point2.x), map_range(i, 0, dist, point1.y, point2.y))
                pygame.gfxdraw.aacircle(screen, int(pos.x), int(pos.y), curr_stroke['brush_size'], curr_stroke['brush_color'])
                pygame.gfxdraw.filled_circle(screen, int(pos.x), int(pos.y), curr_stroke['brush_size'], curr_stroke['brush_color'])
        

    #display button tray
    pygame.draw.rect(screen, (200,200,200), pygame.Rect(0, 0, width, 50))
    plus_button.display()
    minus_button.display()
    black_button.display()
    red_button.display()
    green_button.display()
    green_button.display()
    blue_button.display()
    white_button.display()
    undo_button.display()
    redo_button.display()

    #display mouse brush
    pygame.draw.circle(screen, stroke['brush_color'], mousePos, stroke['brush_size'])
    
    # Flip the display
    pygame.display.flip()


pygame.quit()