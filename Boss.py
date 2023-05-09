import pygame
import random

class Boss:

    def __init__(self):
        self.radius = 85
        self.x = 400
        self.y = 20
        self.speed = 5
        self.Xspeed = random.randint(-15,15)
        self.stop = random.randint(550,800)
        self.stop2 = random.randint(0,250)

    def get_speed(self):
        return self.speed

    def get_location(self):
        return self.x, self.y

    def draw_boss(self,screen,img1):
        img = pygame.image.load(img1)
        img = pygame.transform.scale(img, (self.radius * 2,self.radius * 2))
        screen.blit(img,(self.x,self.y))

    def move(self):
        self.x += self.Xspeed
        if self.x < self.stop2:
            self.x = self.stop2
            self.Xspeed = random.randint(5,12)
            self.stop2 = 0
            self.stop = random.randint(550,800)
        if self.x + self.radius * 2 > self.stop:
            self.x = self.stop - self.radius * 2
            self.Xspeed = random.randint(-12,-5)
            self.stop = 800
            self.stop2 = random.randint(0,250)
