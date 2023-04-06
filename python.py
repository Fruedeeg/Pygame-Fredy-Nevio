import pygame
import random
pygame.init()
win = pygame.display.set_mode((500, 1000))
z = 0
x = 0
v = 0
xplayer = 200
yplayer = 600
xobject = [30]
yobject = [50]
width = 20
height = 20
vel = 2
run = True

def object(xnumber, ynumber):
    pygame.draw.rect(win, (255, 0, 0), (xobject[xnumber], yobject[ynumber], width, height))
    xobject.append(random.randint(0,500))
    yobject.append(random.randint(0,1000))
    
def randomobject(g):
    object(z+g, x+g)
    yobject[g] += 1

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
#    if keys[pygame.K_UP] and y>0:
#        y -= vel
#    if keys[pygame.K_DOWN] and y<500-height:
#        y += vel

    win.fill((0, 0, 0))
    randomobject(0)
    #randomobject(1)
    #randomobject(2)
    #randomobject(3)
    #randomobject(4)
    #randomobject(5)
    #randomobject(6)
    
    if xobject[0] == xplayer and yobject[0] == yplayer:
        win.fill((255, 0, 0))
        pygame.time.wait(200)

    pygame.draw.rect(win, (0, 255, 0), (xplayer, yplayer, width, height))      
    pygame.display.update()
    
pygame.quit()