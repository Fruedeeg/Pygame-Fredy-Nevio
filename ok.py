import pygame
from pygame.locals import*
import random
pygame.init()
win = pygame.display.set_mode((1000, 1000))
z = 0
x = 0
v = 0

rect1 = pygame.Rect(*win.get_rect().center, 0, 0).inflate(75, 75)
rect2 = pygame.Rect(0, 0, 75, 75)

xplayer = 200
yplayer = 600
xobject = [30]
yobject = [50]
width = 20
height = 20
vel = 2
img = pygame.image.load('img.jpg')
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rect2.center = pygame.mouse.get_pos()
    collide = rect1.colliderect(rect2)
    color = (255, 0, 0) if collide else (255, 255, 255)

    win.fill(0)
    pygame.draw.rect(win, color, rect1)
    pygame.draw.rect(win, (0, 255, 0), rect2, 6, 1)
    pygame.display.flip()

pygame.quit()
exit()