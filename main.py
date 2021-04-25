import pygame
import sys
import screen
import person


screen = screen.Screen()
myMonkey = person.Person()


while True:


    screen.drawingBackground(screen.window)

    # Controls

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                myMonkey.walking_left = True
                myMonkey.walking_right = False
            
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                myMonkey.walking_left = False
                myMonkey.walking_right = True


    
    screen.drawingPerson(screen.window, myMonkey)
    screen.limitedPerson(myMonkey)
    myMonkey.walkingPerson()
    
    
    
    screen.updateScreen()

