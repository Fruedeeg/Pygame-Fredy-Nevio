import pygame
from pygame.locals import*
import random
pygame.init()
win = pygame.display.set_mode((1000, 1000))
z = 0
x = 0
v = 0

xplayer = 500
yplayer = 50
xobject = [30]
yobject = [50]
width = 20
height = 20
vel = 2
img = pygame.image.load('img.jpg')
run = True
rect1 = pygame.Rect((xobject[0], yobject[0], width, height))
rect2 = pygame.Rect((xplayer, yplayer, width, height))
def object(xnumber, ynumber):
    pygame.draw.rect(win, (255, 0, 0), (xobject[xnumber], yobject[ynumber], width, height))
    xobject.append(random.randint(0,500))
    yobject.append(random.randint(0,1000))

def randomobject(g):
    object(z+g, x+g)
    xobject[g] += 2

def fail(f):
    if xobject[f] == xplayer:
        win.blit(img,(200,300))
        pygame.display.flip()
        pygame.display.update()
        pygame.time.wait(2000)

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xplayer>0:
        xplayer -= vel
    if keys[pygame.K_RIGHT] and xplayer<500-width:
        xplayer += vel
    if keys[pygame.K_UP] and yplayer>0:
        yplayer -= 30
#    if keys[pygame.K_DOWN] and y<500-height:
#        y += vel
    win.fill(0)
    pygame.draw.rect(win, (0, 255, 0), (xplayer, yplayer, width, height)) 
    randomobject(0)
    #randomobject(1)
    #randomobject(2)
    #randomobject(3)
    #randomobject(4)
    #randomobject(5)
    #randomobject(6)
    fail(0)
    #fail(1)
    #fail(2)
    #fail(3)
    #fail(4)
    #fail(5)
    #fail(6)
    pygame.display.update()
pygame.quit()