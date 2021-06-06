import pygame
import sys
import screen
import person
import banana
import random


screen = screen.Screen()
myMonkey = person.Person()

bananaOne = banana.Banana()
bananaOne.sprites.append(pygame.image.load('../Images/Banana/Banana1.png'))
bananaOne.x = random.randint(0, 900)
bananaOne.y = random.randint(-400, 0)


bananaTwo = banana.Banana()
bananaTwo.sprites.append( pygame.image.load('../Images/Banana/Banana2.png'))
bananaTwo.x = random.randint(0, 900)
bananaTwo.y = random.randint(-400, 0)


bananaThree = banana.Banana()
bananaThree.sprites.append( pygame.image.load('../Images/Banana/Banana3.png') )
bananaThree.x = random.randint(0, 900)
bananaThree.y = random.randint(-400, 0)



allBananas = [ bananaOne, bananaTwo, bananaThree ]

for banana in allBananas:
    banana.sprites[0] = pygame.transform.scale(banana.sprites[0], (20, 20))


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
    
    #Bananas

    
    for banana in allBananas:
        screen.drawingBanana(screen.window, banana)
        banana.fall()
        banana.resetFall()


    #Rect of Monkey

    rectOfMonkey = pygame.draw.rect(screen.window, (20, 50, 80),(myMonkey.x, myMonkey.y + 15, 43, 20))

    #Rect of Bananas

    rectOfBananaOne = pygame.draw.rect(screen.window, (20, 50, 80),(bananaOne.x, bananaOne.y , 20, 20))
    
    rectOfBananaTwo = pygame.draw.rect(screen.window, (20, 50, 80),(bananaTwo.x, bananaTwo.y , 20, 20))
    
    rectOfBananaThree = pygame.draw.rect(screen.window, (20, 50, 80),(bananaThree.x, bananaThree.y , 20, 20))


    for banana in rectOfBananaOne, rectOfBananaTwo, rectOfBananaThree:
        myMonkey.collisionMonkeyBanana(rectOfMonkey, banana)


    screen.updateScreen()

