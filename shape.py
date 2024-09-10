import pygame

class Shape:
    def display(self, pos, scale, color):
        pass

class Plus(Shape):
    def display(self, screen, pos, scale, color):
        pygame.draw.rect(screen, color, pygame.Rect(float(pos.x + 5 * scale - scale/2), float(pos.y), float(scale), float(scale * 10)))
        pygame.draw.rect(screen, color, pygame.Rect(float(pos.x), float(pos.y + 5 * scale - scale/2), float(scale * 10), float(scale)))

class Minus(Shape):
    def display(self, screen, pos, scale, color):
        pygame.draw.rect(screen, color, pygame.Rect(float(pos.x), float(pos.y + 5 * scale - scale/2), float(scale * 10), float(scale)))

class Circle(Shape):
    def display(self, screen, pos, scale, color):
        pygame.gfxdraw.filled_circle(screen, int(pos.x + scale), int(pos.y + scale), scale, color)
        pygame.gfxdraw.aacircle(screen, int(pos.x + scale), int(pos.y + scale), scale, color)

class Arrow_Forward(Shape):
    def display(self, screen, pos, scale, color):
        pygame
        pygame.draw.line(screen, color, pygame.Vector2(pos.x, pos.y + scale / 2), pygame.Vector2(pos.x + scale, pos.y + scale / 2), int(scale / 10))
        pygame.draw.line(screen, color, pygame.Vector2(pos.x + scale / 1.5, pos.y + scale / 5), pygame.Vector2(pos.x + scale, pos.y + scale / 2), int(scale / 10))
        pygame.draw.line(screen, color, pygame.Vector2(pos.x + scale / 1.5, pos.y + (scale - scale / 5)), pygame.Vector2(pos.x + scale, pos.y + scale / 2), int(scale / 10))

class Arrow_Backward(Shape):
    def display(self, screen, pos, scale, color):
        pygame
        pygame.draw.line(screen, color, pygame.Vector2(pos.x, pos.y + scale / 2), pygame.Vector2(pos.x + scale, pos.y + scale / 2), int(scale / 10))
        pygame.draw.line(screen, color, pygame.Vector2(pos.x, pos.y + scale / 2), pygame.Vector2(pos.x + scale - (scale / 1.5), pos.y + scale / 5 ), int(scale / 10))
        pygame.draw.line(screen, color, pygame.Vector2(pos.x, pos.y + scale / 2), pygame.Vector2(pos.x + scale - (scale / 1.5), pos.y + (scale - scale / 5)), int(scale / 10))