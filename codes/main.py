import pygame
import sys
import screen
import person
import banana
import random
import cage


screen = screen.Screen()
myMonkey = person.Person()

bananaOne = banana.Banana()
bananaOne.sprites.append(pygame.image.load('../Images/Banana/Banana1.png'))
bananaOne.x = random.randint(0, 900)
bananaOne.y = random.randint(-400, 0)


bananaTwo = banana.Banana()
bananaTwo.sprites.append(pygame.image.load('../Images/Banana/Banana2.png'))
bananaTwo.x = random.randint(0, 900)
bananaTwo.y = random.randint(-400, 0)


bananaThree = banana.Banana()
bananaThree.sprites.append(pygame.image.load('../Images/Banana/Banana3.png'))
bananaThree.x = random.randint(0, 900)
bananaThree.y = random.randint(-400, 0)


allBananas = [bananaOne, bananaTwo, bananaThree]

cage = cage.Cage()
cage.x = random.randint(0, 900)
cage.y = random.randint(-400, 0)
cage.body = pygame.transform.scale(cage.body, (50, 50))

for banana in allBananas:
    banana.sprites[0] = pygame.transform.scale(banana.sprites[0], (20, 20))

screen.starting_music()
while True:
    # Rect of Monkey

    rectOfMonkey = pygame.draw.rect(screen.window, (20, 50, 80), (myMonkey.x, myMonkey.y + 15, 43, 20))

    # Rect of Bananas

    rectOfBananaOne = pygame.draw.rect(screen.window, (20, 50, 80), (bananaOne.x, bananaOne.y, 20, 20))

    rectOfBananaTwo = pygame.draw.rect(screen.window, (20, 50, 80), (bananaTwo.x, bananaTwo.y, 20, 20))

    rectOfBananaThree = pygame.draw.rect(screen.window, (20, 50, 80), (bananaThree.x, bananaThree.y, 20, 20))

    screen.drawing_background(screen.window)

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

    screen.drawing_person(screen.window, myMonkey)
    screen.limited_person(myMonkey)
    myMonkey.walking_person()
    
    # Bananas

    for banana in allBananas:
        screen.drawing_banana(screen.window, banana)
        banana.fall()
        banana.reset_fall()

    # Cage
    screen.drawing_cage(screen.window, cage)
    cage.fall()
    cage.reset_fall()

    # Rect of Monkey

    #rectOfMonkey = pygame.draw.rect(screen.window, (20, 50, 80), (myMonkey.x, myMonkey.y + 15, 43, 20))

    # Rect of Bananas

    #rectOfBananaOne = pygame.draw.rect(screen.window, (20, 50, 80), (bananaOne.x, bananaOne.y, 20, 20))
    
    #rectOfBananaTwo = pygame.draw.rect(screen.window, (20, 50, 80), (bananaTwo.x, bananaTwo.y, 20, 20))
    
    #rectOfBananaThree = pygame.draw.rect(screen.window, (20, 50, 80), (bananaThree.x, bananaThree.y, 20, 20))

    myMonkey.collision_monkey_banana(rectOfMonkey, bananaOne, rectOfBananaOne)
    myMonkey.collision_monkey_banana(rectOfMonkey, bananaTwo, rectOfBananaTwo)
    myMonkey.collision_monkey_banana(rectOfMonkey, bananaThree, rectOfBananaThree)

    # Show bananas of monkey in display

    screen.show_bananas(myMonkey)

    screen.update_screen()
