import pygame
import random

class Box:

    def __init__(self):
        self.width = 200
        self.height = 145
        self.x = random.randint(50,600)
        self.y = 655

    def get_location(self):
        return self.x, self.y

    def draw_box(self, screen):
        bg = pygame.image.load("img/Cart.jpg")
        bg = pygame.transform.scale(bg, (self.width,self.height))
        screen.blit(bg, (self.x,self.y))

    def move_left(self):
        self.x -= 25
        if self.x <= 0:
            self.x = 0

    def move_right(self):
        self.x += 25
        if self.x >= 625:
            self.x = 625
