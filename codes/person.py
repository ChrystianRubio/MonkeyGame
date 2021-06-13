import pygame
import random


class Person:
    def __init__(self):
        
        self.sprites = [pygame.image.load('../Images/Monkey/monkey_right1.png'),
                        pygame.image.load('../Images/Monkey/monkey_right3.png'),
                        ]
        
        self.anySprite = 0
        self.body = self.sprites[self.anySprite]

        self.x = 50
        self.y = 298
        self.walking_right = self.walking_left = False
        self.get_banana = 0
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
            random_for_song = random.randint(0, 400)

            if random_for_song <= 100:
                self.collision_banana_song.play()

    def collision_monkey_cage(self, cage, rect_of_monkey, rect_of_cage):
        if pygame.Rect.colliderect(rect_of_monkey, rect_of_cage):
            self.get_banana = 0
            cage.y = random.randint(-600, 0)
            cage.x = random.randint(0, 900)
            self.collision_cage_song.play()
