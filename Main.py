import pygame
import sys
pygame.display.set_caption("Title")
pygame.init()

width = 1000
height = 1000
window = pygame.display.set_mode((width, height))

pygame.mixer.music.load("06 - Ready Funk - Yuzo Koshiro.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

successSound = pygame.mixer.Sound("success.mp3")
successSound.set_volume(2)
wooshSound = pygame.mixer.Sound("fireswoosh.ogg")
wooshSound.set_volume(0.5)


cursor = pygame.image.load("cursor.png")
cursor = pygame.transform.scale(cursor, (30, 30))
pygame.mouse.set_cursor((13,13),cursor)

logo = pygame.image.load("drawing.png").convert_alpha()
logo_x = (width - logo.get_width()) // 2
logo_y = 50

menuBG = pygame.image.load("menubg.jpg").convert()
menuBG = pygame.transform.scale(menuBG, (width, height))
menuBG2 = pygame.image.load("menubg2.jpg").convert()

clock = pygame.time.Clock()
xButton = width // 2 - 250
yButton = height // 2 - 25

black = 0,0,0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 150, 0
x = logo.get_width()
y = logo.get_height()
show_title = True
counter = 0
counter2 = 0
up = False 
upVel = 0.5
downVel = 1
lvl1 = 0
lvl2 = 0
lvl3 = 0
impact = 20
impactCount = 0

while show_title:
    
    window.fill(white)
    anyButton = pygame.Rect(xButton, yButton, 500, 70)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            show_title = False
            sys.exit()
            
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            successSound.play()
            wooshSound.play()

            for i in range(0, 100):
                window.blit(pygame.transform.scale(logo , (x, y)), (logo_x, logo_y))
                x *= 1.016
                y *= 1.016
                pygame.display.flip()
                window.fill(white)
                
            logo_y -= 20
            
            for i in range(0, 270):
                window.blit(pygame.transform.scale(logo , (x, y)), (logo_x, logo_y))
                logo_x -= 13
                pygame.display.flip()
                window.fill(white)
                
            logo_x += 3510
            pygame.mixer.music.fadeout(2000)
            
            for i in range(0, 100):
                window.blit(pygame.transform.scale(logo , (x, y)), (logo_x, logo_y))
                x *= 0.984
                y *= 0.984
                pygame.display.flip()
                window.fill(white)
            pygame.time.wait(500)
            import Menu
            Menu()
    
    counter += 1
    if counter < 40:
        yButton -= upVel
    if counter > 40 < 60:
        yButton += downVel
    if counter == 60:
        counter = 0
    lvl0 = 0.025* pygame.mouse.get_pos()[0]-width/80
    lvl1 = 0.05* pygame.mouse.get_pos()[0]-width/40
    lvl2 = 0.1*pygame.mouse.get_pos()[0]-width/20
    lvl3 = 0.25*pygame.mouse.get_pos()[0]-width/8
    
    
    pygame.draw.rect(window, (120,120,120), pygame.Rect(lvl0, 350+pygame.mouse.get_pos()[1]/30, 1000, 100))
    pygame.draw.rect(window, (100,100,100), pygame.Rect(lvl1, 450+pygame.mouse.get_pos()[1]/30, 1000, 100))
    pygame.draw.rect(window, (80,80,80), pygame.Rect(lvl2, 550+pygame.mouse.get_pos()[1]/30, 1000, 100))
    pygame.draw.rect(window, (60,60,60), pygame.Rect(lvl3, 650+pygame.mouse.get_pos()[1]/30, 1000, 100))
    #window.blit(lvl0IMG, (lvl0, 0))
    #window.blit(lvl1IMG, (lvl1, 0))
    #window.blit(lvl2IMG, (lvl2, 0))
    #window.blit(lvl3IMG, (lvl3, 0))

    
    
    window.blit(logo, (logo_x+impact, logo_y))
    impactCount += 1
    
    if impactCount == 15:
        impact *=-0.9
        impactCount = 0
    
    
    font = pygame.font.SysFont('Arial', 35)
    text = font.render("Press any Button", True, white)
    #pygame.draw.rect(window, black, (xButton+50, yButton+60, 400, 10), border_radius=10)
    pygame.draw.rect(window, (200, 20, 20), anyButton, border_radius=10)
    pygame.draw.rect(window, black, anyButton, border_radius=10, width=4)
    text_rect = text.get_rect()
    text_rect.center = anyButton.center
    window.blit(text, text_rect)
    
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
