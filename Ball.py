import pygame
import random

class Ball:

    def __init__(self):
        self.radius = 25
        self.x = random.randint(0,750)
        self.y = 40
        self.speed = 5
        self.Xspeed = 0

    def get_speed(self):
        return self.speed

    def get_location(self):
        return self.x, self.y

    def set_y(self,y):
        self.y = y

    def set_x(self,x):
        self.x = x


    def draw_ball(self,screen,img1):
        img = pygame.image.load(img1)
        img = pygame.transform.scale(img, (self.radius * 2,self.radius * 2))
        screen.blit(img, (self.x, self.y))

    def draw_boom(self,screen):
        img = pygame.image.load("img/boom.png")
        img = pygame.transform.scale(img, (self.radius * 4.5,self.radius * 3))
        screen.blit(img, (self.x, self.y - 50))

    def shoot(self):
        self.y -= self.speed
        return self.y >= 0

    def move_down(self):
        self.y += self.speed
        return self.y >= 730

    def SetXspeed(self,x):
        self.Xspeed = x

    def Set_speed(self,x):
        self.speed = x

    def collision(self):
        if self.x < 0:
            self.x = 0
            self.Xspeed = -self.Xspeed
        if self.x + 50 > 800:
            self.x = 750
            self.Xspeed = -self.Xspeed

    def MoveHori(self,Angle):
        if Angle != 90:
            self.x += self.Xspeed

    def reset(self, x,y):
        self.y = y
        self.speed += 0.5
        self.x = x
