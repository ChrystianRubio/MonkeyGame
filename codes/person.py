import pygame
import random


class Person:
    def __init__(self):
        
        self.sprites = [
                        pygame.image.load('../Images/Monkey/monkey_right1.png'),
                        pygame.image.load('../Images/Monkey/monkey_right3.png'),
                       ]
        
        self.anySprite = 0
        self.body = self.sprites[self.anySprite]

        self.x = 50
        self.y = 298
        self.walking_right = self.walking_left = False

        self.get_banana = 0
        self.life = 3
        self.speed = 1.5

        self.collision_banana_song = pygame.mixer.Sound('../Songs/monkey_imitation.wav')
        self.collision_cage_song = pygame.mixer.Sound('../Songs/monkey_cry.wav')
    
    def walking_person(self):
        
        if self.walking_left:
            self.x -= self.speed
            self.anySprite += 0.02

            if self.anySprite >= 2:
                self.anySprite = 0

            # Animations
            
            self.body = self.sprites[int(self.anySprite)]

        if self.walking_right:
            self.x += self.speed
            self.anySprite += 0.02

            if self.anySprite >= 2:
                self.anySprite = 0

            # Animations
            
            self.body = pygame.transform.flip(self.sprites[int(self.anySprite)], True, False)

    def collision_monkey_banana(self, rect_of_monkey, banana, rect_of_banana):
        if pygame.Rect.colliderect(rect_of_monkey, rect_of_banana):
            self.get_banana += 1
            banana.y = random.randint(-400, 0)
            banana.x = random.randint(0, 900)

    def collision_monkey_cage(self, cage1, cage2, rect_of_monkey, rect_of_cage, rect_of_cage2):
        if pygame.Rect.colliderect(rect_of_monkey, rect_of_cage):
            cage1.y = random.randint(-600, 0)
            cage1.x = random.randint(0, 900)
            cage1.speed = cage2.speed = 1.6
            self.life -= 1
            self.collision_cage_song.play()

        if pygame.Rect.colliderect(rect_of_monkey, rect_of_cage2):
            cage2.y = random.randint(-600, 0)
            cage2.x = random.randint(0, 900)
            cage1.speed = cage2.speed = 1.6
            self.life -= 1
            self.collision_cage_song.play()

    def collision_monkey_heart(self, heart, rect_of_monkey, rect_of_heart):
        if pygame.Rect.colliderect(rect_of_monkey, rect_of_heart):
            self.life += 1
            heart.y = random.randint(-600, 0)
            heart.x = random.randint(0, 900)
            heart.speed = 1.6

            random_for_song = random.randint(0, 400)
            # sound monkey random
            if random_for_song <= 100:
                self.collision_banana_song.play()
