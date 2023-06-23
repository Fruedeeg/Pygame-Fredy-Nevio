import pygame
import sys
import random
pygame.display.set_caption("game")
pygame.init()
pygame.mixer.stop()
pygame.mixer.music.stop()
pygame.mixer.music.load("01 - Player Select V2 - Yuzo Koshiro.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

width = 1000
height = 1000
playing = 0
playing2 = 0
playing3 = 0
window = pygame.display.set_mode((width, height))

cursor = pygame.image.load("cursor.png")
cursor = pygame.transform.scale(cursor, (30, 30))
pygame.mouse.set_cursor((13,13),cursor)

successSound = pygame.mixer.Sound("success.mp3")
clickSound = pygame.mixer.Sound("mech.mp3")
clickSound.set_volume(0.5)

flushSound = pygame.mixer.Sound("flush.mp3")
flushSound.set_volume(0.7)
clicksound2 = pygame.mixer.Sound("mech2.mp3")
clicksound2.set_volume(0.5)
logo = pygame.image.load("FredyGame.png").convert_alpha()
logo_x = (width - logo.get_width()) // 2
logo_y = 50

menuBG = pygame.image.load("menubg.jpg").convert()
menuBG = pygame.transform.scale(menuBG, (width, height))
menuBG2 = pygame.image.load("menubg2.jpg").convert()
menuBG2 = pygame.transform.scale(menuBG2, (width, height))
blueImg = pygame.image.load("blue.png")
blueImg = pygame.transform.scale(blueImg, (width, height))

clock = pygame.time.Clock()

playButton = pygame.Rect(width // 2 - 100, height // 2 - 25, 205, 50)
quitButton = pygame.Rect(width // 2 - 100, height // 2 + 50, 205, 50)
musicButton = pygame.Rect(width // 2 - 100, height // 2 + 125, 205, 50)
black = 0,0,0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 150, 0
selected_button = 0
show_menu = True

frame = 0


while show_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flushSound.play()
            show_menu = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if playButton.collidepoint(x, y):
            successSound.play()
            for i in range(0,10):
                window.blit(pygame.transform.scale(pygame.image.load("menubganim/frame000" +str(frame)+ ".jpg"), (width, height)), (0,0))
                pygame.display.flip()
                pygame.time.delay(30)
                frame += 1
            for i in range(0,3):
                window.blit(pygame.transform.scale(pygame.image.load("menubganim/frame00" +str(frame)+ ".jpg"), (width, height)), (0,0))
                pygame.time.delay(30)
                pygame.display.flip()
                frame += 1
            pygame.mixer_music.fadeout(1000)
            show_menu = False
            pygame.mixer.music.stop()
            import Game
            Game()
        elif quitButton.collidepoint(x, y):
            flushSound.play()
            window.blit(blueImg, (0, 0))
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.quit()
            sys.exit()
        elif musicButton.collidepoint(x, y):
            import Music
            Music()
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            selected_button = 0
        elif event.key == pygame.K_DOWN:
            selected_button = 1
        elif event.key == pygame.K_RETURN:
            if selected_button == 0:
                clickSound.play()
                for i in range(0,10):
                    window.blit(pygame.transform.scale(pygame.image.load("menubganim/frame000" +str(frame)+ ".jpg"), (width, height)), (0,0))
                    pygame.display.flip()
                    pygame.time.delay(30)
                    frame += 1
                for i in range(0,3):
                    window.blit(pygame.transform.scale(pygame.image.load("menubganim/frame00" +str(frame)+ ".jpg"), (width, height)), (0,0))
                    pygame.time.delay(30)
                    pygame.display.flip()
                    frame += 1
                pygame.mixer_music.fadeout(1000)
                show_menu = False
                import Cleaner
                Cleaner.main()
                break
            elif selected_button == 1:
                flushSound.play()
                pygame.quit()
                sys.exit()
            elif selected_button == 3:
                import Music
                Music()
    if playButton.collidepoint(pygame.mouse.get_pos()):
        selected_button = 0
        green = 100, 170, 100
        if playing == 0:
            clickSound.play()
            playing = 1
    else: 
        green = 0, 150, 0
        playing = 0
    if quitButton.collidepoint(pygame.mouse.get_pos()):
        selected_button = 1
        red = 255, 100, 100
        if playing2 == 0:
            clicksound2.play()
            playing2 = 1
    else:
        red = 255, 0, 0
        playing2 = 0
    if musicButton.collidepoint(pygame.mouse.get_pos()):
        selected_button = 3
        blue = 100, 100, 255
        if playing3 == 0:
            clickSound.play()
            playing3 = 1
    else:
        blue = 50, 50, 255
        playing3 = 0
    if selected_button == 0 or selected_button == 3:
        window.blit(menuBG, (0, 0))
    else:
        window.blit(menuBG2, (0, 0))
    
    window.blit(logo, (logo_x, logo_y))
    font = pygame.font.SysFont('Liberation Sans', 35)
    text = font.render("Start", True, white)
    pygame.draw.rect(window, green, playButton, border_radius=10)
    if selected_button == 0:
        pygame.draw.rect(window, black, playButton, border_radius=10, width=4)
    text_rect = text.get_rect()
    text_rect.center = playButton.center
    window.blit(text, text_rect)
    text = font.render("Exit", True, white)
    pygame.draw.rect(window, red, quitButton, border_radius=10)
    if selected_button == 1:
        pygame.draw.rect(window, black, quitButton, border_radius=10, width=4)
    text_rect = text.get_rect()
    text_rect.center = quitButton.center
    window.blit(text, text_rect)
    text = font.render("Music", True, white)
    pygame.draw.rect(window, blue, musicButton, border_radius=10)
    if selected_button == 3:
        pygame.draw.rect(window, black, musicButton, border_radius=10, width=4)
    text_rect = text.get_rect()
    text_rect.center = musicButton.center
    window.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
