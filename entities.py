import pygame
class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Coin:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)    

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
