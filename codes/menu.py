import pygame
import sys


def menu():
    pygame.init()
    janela = pygame.display.set_mode((1000, 339)) #800, 600
    pygame.display.set_caption('Menu')
    icon_da_janela = pygame.image.load('../Images/Monkey/monkey_icon.png')
    pygame.display.set_icon(icon_da_janela)
    janela.fill((0, 0, 0))

    flag = True
    pos0 = pos1 = 0

    msg = pygame.font.Font('freesansbold.ttf', 70)
    msg_inicial = msg.render('Monkey Game', True, (128, 128, 140))
    foto_para_menu = pygame.image.load('../Images/Monkey/monkeyForest2.png')
    foto_para_menu = pygame.transform.scale(foto_para_menu, (200, 200))

    msg2_corpo = pygame.draw.rect(janela, (128, 128, 140), (400, 125, 380, 50))
    msg2 = pygame.font.Font('freesansbold.ttf', 50)
    msg2_botao = msg2.render('START', True, (0, 0, 0))

    msg3_corpo = pygame.draw.rect(janela, (128, 128, 140), (400, 185, 380, 50))
    msg3 = pygame.font.Font('freesansbold.ttf', 50)
    msg3_botao = msg3.render('SOBRE', True, (0, 0, 0))

    msg4_corpo = pygame.draw.rect(janela, (128, 128, 140), (400, 245, 380, 50))
    msg4 = pygame.font.Font('freesansbold.ttf', 50)
    msg4_botao = msg4.render('RECORDES', True, (0, 0, 0))

    flag_de_tela = False
    botao_de_volta = pygame.draw.rect(janela, (128, 128, 140), (0, 550, 100, 30))

    while flag:

        # Eventos de teclado
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos0 = pygame.mouse.get_pos()[0]
                pos1 = pygame.mouse.get_pos()[1]

        mouse = pygame.draw.rect(janela, (128, 128, 140), (pos0, pos1, 20, 20))

        if not flag_de_tela:
            janela.fill((0, 0, 0))
            msg2_corpo = pygame.draw.rect(janela, (128, 128, 140), (400, 125, 380, 50))
            msg2_botao = msg2.render('START', True, (0, 0, 0))
            msg3_corpo = pygame.draw.rect(janela, (128, 128, 140), (400, 185, 380, 50))
            msg3_botao = msg3.render('SOBRE', True, (0, 0, 0))
            msg4_corpo = pygame.draw.rect(janela, (128, 128, 140), (400, 245, 380, 50))
            msg4_botao = msg4.render('RECORDES', True, (0, 0, 0))

            janela.blit(foto_para_menu, (80, 100))
            janela.blit(msg_inicial, (339/2, 20))
            janela.blit(msg2_botao, (500, 130))
            janela.blit(msg3_botao, (490, 186))
            janela.blit(msg4_botao, (460, 246))

        if pygame.Rect.colliderect(msg2_corpo, mouse):
            flag = False

        # aqui para fazer o botao de recorder funcionar


        if pygame.Rect.colliderect(msg3_corpo, mouse):
            flag_de_tela = True

            janela.fill((0, 0, 0))

            botao_de_volta = pygame.draw.rect(janela, (128, 128, 140), (0, 310, 100, 30))
            logo_do_pygame = pygame.image.load('../Images/background/pygame_logo.png')
            sobre = pygame.font.Font('freesansbold.ttf', 20)
            sobre_render = sobre.render('CRIADO POR: CHRYSTIAN RUBIO', True, (120, 120, 120))
            sobre_render2 = sobre.render('DESENHOS: www.flaticon.com', True, (120, 120, 120))
            sobre_render3 = sobre.render('MUSICAS: freesound.org', True, (120, 120, 120))
            sobre_render4 = sobre.render('FRAMEWORK: www.pygame.org', True, (120, 120, 120))
            msg_de_volta = sobre.render('VOLTAR', True, (0, 0, 0))

            janela.blit(sobre_render, (0, 50))
            janela.blit(sobre_render2, (0, 125))
            janela.blit(sobre_render3, (0, 190))
            janela.blit(sobre_render4, (0, 260))
            janela.blit(logo_do_pygame, (500, -50))
            janela.blit(msg_de_volta, (10, 320))

        if pygame.Rect.colliderect(botao_de_volta, mouse):
            flag_de_tela = False

        pygame.display.update()
