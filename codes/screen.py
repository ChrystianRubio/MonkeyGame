import pygame


class Screen:
    def __init__(self):

        pygame.init()
        self.size = (1000, 400) #100, 400
        self.colorScreen = (100, 0, 25)
        self.title = 'Monkey'
        self.background = pygame.image.load('./Images/background/background_forest.jpeg')
        #self.background = pygame.transform.scale(self.background, (1000, 600))
        self.window = pygame.display.set_mode(self.size)
        self.control_frames = pygame.time.Clock()
        pygame.display.set_caption(self.title)


    def drawingBackground(self, screenColor):
        screenColor.blit(self.background, (0, 0))


    def updateScreen(self):
        pygame.display.update()
        self.control_frames.tick(120)


    def drawingPerson(self, screen, person):
        screen.blit(person.body, (person.x, person.y))


    def limitedPerson(self, person):
        
        if person.x <= -5:
            person.x = -5 
        
        if person.x >= 955:
            person.x = 955
