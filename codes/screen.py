import pygame


class Screen:
    def __init__(self):

        pygame.init()
        self.size = (1000, 339) 
        self.colorScreen = (100, 0, 25)
        self.title = 'Monkey'
        self.background = pygame.image.load('../Images/background/background_forest.jpeg')
        # self.background = pygame.transform.scale(self.background, (1000, 600))
        self.window = pygame.display.set_mode(self.size)
        self.control_frames = pygame.time.Clock()
        pygame.mixer.music.load('../Songs/monkey_music.wav')
        pygame.display.set_caption(self.title)

    def drawing_background(self, screen_color):
        screen_color.blit(self.background, (0, 0))

    def update_screen(self):
        pygame.display.update()
        self.control_frames.tick(120)

    @staticmethod
    def drawing_person(screen, person):
        screen.blit(person.body, (person.x, person.y))

    @staticmethod
    def drawing_banana(screen, banana):
        screen.blit(banana.sprites[0], (banana.x, banana.y))

    @staticmethod
    def drawing_cage(screen, cage):
        screen.blit(cage.body, (cage.x, cage.y))

    @staticmethod
    def limited_person(person):

        if person.x <= -5:
            person.x = -5 
        
        if person.x >= 955:
            person.x = 955

    def show_bananas(self, monkey):
        msg_font = pygame.font.Font('freesansbold.ttf', 25)
        msg_show = msg_font.render('Bananas: ' + str(monkey.get_banana), True, (100, 200, 100))
        self.window.blit(msg_show, (0, 10))

    @staticmethod
    def starting_music():
        pygame.mixer.music.play(-1)
