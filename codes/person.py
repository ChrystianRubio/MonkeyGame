import pygame


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
        self.life = 3
        self.speed = 1.5
    
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

    def collision_monkey_banana(self, rect_of_monkey, banana):
        if pygame.Rect.colliderect(rect_of_monkey, banana):
            print('Testing collision')
