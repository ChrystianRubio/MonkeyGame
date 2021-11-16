import pygame
import random


class Cage:
    def __init__(self):

        self.body = pygame.image.load('../Images/Cage/cage.png')
        self.x = 0
        self.y = 0
        self.speed = 1.6

    def fall(self):
        self.y += self.speed

    def reset_fall(self):
        if self.y >= 410:
            self.x = random.randint(0, 900)
            self.y = random.randint(-400, 0)
            self.speed += 0.1
