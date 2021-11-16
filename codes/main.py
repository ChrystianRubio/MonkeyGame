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

cage1 = cage.Cage()
cage1.x = random.randint(0, 900)
cage1.y = random.randint(-400, 0)
cage1.body = pygame.transform.scale(cage1.body, (50, 50))

cage2 = cage.Cage()
cage2.x = random.randint(0, 900)
cage2.y = random.randint(-400, 0)
cage2.body = pygame.transform.scale(cage2.body, (50, 50))

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

    # Rect of Cage

    rectOfCage1 = pygame.draw.rect(screen.window, (20, 50, 80), (cage1.x, cage1.y + 15, 43, 20))
    rectOfCage2 = pygame.draw.rect(screen.window, (20, 50, 80), (cage2.x, cage2.y + 15, 43, 20))

    # Background
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

            if event.key == pygame.K_SPACE:
                myMonkey.speed = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                myMonkey.walking_left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                myMonkey.walking_right = False
            if event.key == pygame.K_SPACE:
                myMonkey.speed = 1.5

    screen.drawing_person(screen.window, myMonkey)
    screen.limited_person(myMonkey)
    myMonkey.walking_person()
    
    # Bananas

    for banana in allBananas:
        screen.drawing_banana(screen.window, banana)
        banana.fall()
        banana.reset_fall()

    # Cage
    screen.drawing_cage(screen.window, cage1)
    cage1.fall()
    cage1.reset_fall()

    screen.drawing_cage(screen.window, cage2)
    cage2.fall()
    cage2.reset_fall()

    myMonkey.collision_monkey_banana(rectOfMonkey, bananaOne, rectOfBananaOne)
    myMonkey.collision_monkey_banana(rectOfMonkey, bananaTwo, rectOfBananaTwo)
    myMonkey.collision_monkey_banana(rectOfMonkey, bananaThree, rectOfBananaThree)

    myMonkey.collision_monkey_cage(cage1, rectOfMonkey, rectOfCage1)
    myMonkey.collision_monkey_cage(cage2, rectOfMonkey, rectOfCage2)

    # Show bananas of monkey in display

    screen.show_bananas(myMonkey)

    screen.update_screen()
