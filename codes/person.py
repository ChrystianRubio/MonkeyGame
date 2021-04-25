import pygame


class Person:
    def __init__(self):
        
        self.sprites = [ pygame.image.load('./Images/Monkey/monkey_right1.png') ,
                         
                         pygame.image.load('./Images/Monkey/monkey_right3.png') ,
                        ]


        #for image in range(0, len(self.sprites)):
         #   self.sprites[image] = pygame.transform.scale(self.sprites[image], (100, 73))
        
        self.anySprite = 0
        self.body = self.sprites[self.anySprite]

        self.x = 50
        self.y = 300
        self.walking_right =  self.walking_left = False

        self.life = 3
    
    def walkingPerson(self):
        
        if self.walking_left:
            self.x -= 2
            self.anySprite += 0.02

            if self.anySprite >= 2:
                self.anySprite = 0

             #Animations
            
            self.body = self.sprites[int(self.anySprite)]
            


        if self.walking_right:
            self.x += 2
            self.anySprite += 0.02

            if self.anySprite >= 2:
                self.anySprite = 0

            #Animations
            
            self.body = pygame.transform.flip(self.sprites[int(self.anySprite)], True , False)
        
       




