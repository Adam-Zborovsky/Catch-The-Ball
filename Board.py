from Ball import Ball
from Box import Box
from Boss import Boss
import random
import math
import pygame


class Board:

    def __init__(self):
        self.height = 800
        self.width = 800
        self.ball = Ball()
        self.box = Box()
        self.boss = Boss()
        self.interval = 35
        self.screen = pygame.display.set_mode([self.width, self.height])

    def ball_touches_box(self):
        return self.box.get_location()[0] - 30 <= self.ball.get_location()[0] <= self.box.get_location()[0] + 200 and \
               self.ball.get_location()[1] >= 665

    def ball_touches_boss(self):
        return self.boss.get_location()[0] - 50 <= self.ball.get_location()[0] <= self.boss.get_location()[0] + 170 and \
            145 <= self.ball.get_location()[1] <= 170

    def play_boss(self, time):
        balls = ["img/Banana.png", "img/Pie.png", "img/SS.jpg", "img/strawberry.png", "img/lettuce.png",
                 "img/halbon.png", "img/carrot.png", "img/bread.png", "img/aplepe.png"]
        i = random.randint(0, 8)
        c = 0
        hp = 5
        hp *= time
        running = True
        shoot = False
        clock = pygame.time.Clock()
        bg = pygame.image.load("img/BG.png")
        bg = pygame.transform.scale(bg, (800, 800))
        while running:
            SavedI = i
            pygame.display.set_caption('Catch The ball:' + "    Press Space To Shoot" + "                                    HP: " + "❤" * hp)
            clock.tick(self.interval)
            self.screen.blit(bg, (0, 0))
            self.ball.draw_ball(self.screen, balls[i])
            self.box.draw_box(self.screen)
            self.boss.draw_boss(self.screen, "img/cash.png")
            self.boss.move()
            roof = self.ball.get_location()[1] <= 0
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        shoot = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.box.move_left()
            if keys[pygame.K_RIGHT]:
                self.box.move_right()
            if not shoot:
                self.ball.set_x(self.box.get_location()[0] + 90)
                self.ball.set_y(self.box.get_location()[1] + 25)
            if not self.ball_touches_boss() and shoot:
                shoot = self.ball.shoot()
            if self.ball_touches_boss():
                i = random.randint(0, 8)
                while i == SavedI:
                    i = random.randint(0, 8)
                hp -= 1
                shoot = False
                self.ball.reset(self.box.get_location()[0] + 90, self.box.get_location()[1] + 50)
                c += 1
            if roof:
                i = random.randint(0, 8)
                while i == SavedI:
                    i = random.randint(0, 8)
                self.ball.reset(self.box.get_location()[0] + 90, self.box.get_location()[1] + 50)
                c += 1
            if hp == 0:
                pygame.display.set_caption(
                    'Catch The ball' + "                                                                        GOOD JOB, YOU MAY CONTINUE SHOPPING")
                pygame.time.delay(2000)
                running = False

        pygame.display.flip()
        return c // 2

    def play(self):
        Angle = 90
        Xspeed = 0
        balls = ["img/bomb.png", "img/Banana.png", "img/Pie.png", "img/SS.jpg", "img/strawberry.png", "img/lettuce.png",
                 "img/halbon.png","img/carrot.png", "img/bread.png", "img/aplepe.png"]
        noob = 0
        pro = 0
        lastboss = 0
        time = 1
        i = random.randint(0,9)
        running = True
        clock = pygame.time.Clock()
        bg = pygame.image.load("img/BG.png")
        bg = pygame.transform.scale(bg, (800, 800))
        while running:
            savedI = i
            pygame.display.set_caption(
                'Catch The ball' + '                                         Caught =' + str(
                    pro) + '                           UnCaught = ' + str(noob) + "                           Bosses Defeated = " + str(time - 1))
            clock.tick(self.interval)
            self.screen.blit(bg, (0, 0))
            self.ball.draw_ball(self.screen, balls[i])
            self.box.draw_box(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.box.move_left()
            if keys[pygame.K_RIGHT]:
                self.box.move_right()
            if pro != lastboss and pro != 0 and pro % 10 == 0:
                self.ball.Set_speed(self.ball.get_speed() - 0.5 * self.play_boss(time))
                time += 1
                lastboss = pro
            floor = self.ball.move_down()
            self.ball.MoveHori(Angle)
            self.ball.collision()
            if self.ball_touches_box():
                if i == 0:
                    pygame.display.set_caption(
                        'Catch The ball' + "                                                                             BOOM, YOU LOST 3 POINTS")
                    pro -= 3
                    pygame.time.delay(2000)
                Angle = random.randint(-200, 200)
                Xspeed = int(math.cos(Angle * (math.pi / 180)) * self.ball.get_speed())
                self.ball.SetXspeed(Xspeed)
                i = random.randint(0,9)
                while i == savedI:
                    i = random.randint(0,9)
                self.ball.reset(random.randint(0,750), 40)
                if i != 0:
                    pro += 1
            if floor:
                Angle = random.randint(-155, 155)
                self.ball.SetXspeed(Xspeed)
                if i != 0:
                    noob += 1
                i = random.randint(0,9)
                while i == savedI:
                    i = random.randint(0,9)
                self.ball.reset(random.randint(0,750),40)
                if noob >= 40:
                    pygame.display.set_caption(
                        'Catch The ball' + "                                                                                    YOU LOSE")
                    pygame.time.delay(2000)
                    running = False

            pygame.display.flip()
