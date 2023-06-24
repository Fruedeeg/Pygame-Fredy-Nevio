import pygame
import math
import random
pygame.init()
width = 1000
height = 1000
smallHeight = 500
smallWidth = 500
window = pygame.display.set_mode((width, height))
smallWindow = pygame.Surface((smallWidth, smallHeight))
tileRects = []
clock = pygame.time.Clock()
walkrect = pygame.Rect(100, 100, 32, 32)

walkCurrent = 0
jumpSound = pygame.mixer.Sound("jumpsound.mp3")
jumpSound.set_volume(0.3)
jumpSoundPlaying = False

shootSound = pygame.mixer.Sound("gunshot.ogg")
shootSound.set_volume(0.3)

emptySound = pygame.mixer.Sound("emptygun.mp3")
emptySound.set_volume(0.5)
emptyPlaying = False
swhooshSound = pygame.mixer.Sound("whoosh.mp3")
swhooshSound.set_volume(0.5)

hitSound = pygame.mixer.Sound("hit.ogg")
hitSound.set_volume(0.3)
hitPlaying = False
hitCount = 0
tileY = 0

walk = pygame.image.load("forward_idle.png")
walkRight = pygame.image.load("walk_right.png")
walkLeft = pygame.image.load("walk_left.png")
roll = pygame.image.load("roll.png")

isRemoved = True
logo = pygame.image.load("youFailed.png")
logo_x = (width - logo.get_width()) // 2
logo_y = 0
logoX = logo.get_width()
logoY = logo.get_height()

ammoImg = pygame.image.load("ammo.png") 
ammoImg = pygame.transform.scale(ammoImg, (37/1.5, 32/1.5))

pygame.mixer.music.load("02 - Go Straight - Yuzo Koshiro.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
pygame.mixer.music.play
idleframe = 0
tilecount =0
dashCounter = 0

map1 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','7','2','2','2','2','2','2','2','2','2','2','2','6','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','3','4','4','4','4','4','5','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','1','1','0','0','0','0','0','7','2','2','6','0','0','0','0','0','0','0',],
        ['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2',],
        ['0','0','1','1','2','2','2','2','2','2','2','2','0','0','0','2','2','2','1','1',],
        ['0','0','1','1','1','1','1','1','1','1','1','1','0','0','0','1','1','1','1','1',]]

map2 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','2','2','2','2','2','2','2','2','2','2','2','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','2','2','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2',],
        ['0','0','0','0','2','2','2','2','2','2','2','2','0','0','0','2','2','2','1','1',],
        ['0','0','0','0','1','1','1','1','1','1','1','1','0','0','0','1','1','1','1','1',]]


# def idleanim:
#     window.blit((pygame.image.load("player2/playeranim000"+ str(idleframe)+ ".png")), player)
#     playerImage = window.blit((pygame.image.load("player2/playeranim000"+ str(idleframe)+ ".png")), player)


cursorWhite = pygame.image.load("cursornewWhite.png")
cursor = pygame.image.load("cursornew.png")
pygame.mouse.set_cursor((12, 12),cursor)
smallCursor = pygame.image.load("smallCursor.png")
smallCursorWhite= pygame.image.load("smallCursorWhite.png")

font = pygame.font.Font("fonts/Wellbutrin.ttf", 10)
bigFont = pygame.font.Font("fonts/Wellbutrin.ttf", 20)


x = 250
y = 250
finalScore = 0
white = (255, 255, 255)
black = (0, 0 ,0)
green = (0, 255, 0)
red = (255, 0, 0)

jumping = False
canJump = True
left = False
right = False
collision = False

gravity = 0.5
fastest = 0

shoot = False
bullets = []
bulletCounter = 0
bulletSpeed = 5
bulletRadius = 3
bulletDelay = 10
falling = False
doubleJump = True
doubleCount = 0
doubleCount2 =0
last = True
knockback = 2
y_Velocity = 0
leftVelocity = 0
rightVelocity = 0
maxSpeed = 4
acceleration = 0.15
jumpHeight = 8
frame = 0
counter = 0

particleDuration = 20
shot = 0
Ammo = 40
floorX = 0
score = 0
tilesize = 25


scoreText = font.render("Score: " + str(score), True, black)
scoreRect = scoreText.get_rect()
scoreRect.topright = (smallWidth-59, -smallHeight+50)

ammoText = font.render(f"Ammunition:{Ammo}", True, black)
ammoRect = ammoText.get_rect()
ammoRect.topleft = (25, 25)

pausedText = bigFont.render("Paused", True, white)
pausedRect = pausedText.get_rect()
pausedRect.center = (smallWidth/2, smallHeight/2)

color = black
pauseText = font.render("Pause", True, color)
pauseRect = pausedText.get_rect()
pauseRect.center = (smallWidth-pausedRect.width, 25)

grass = pygame.image.load("Tiles/grassMid.png")
grass = pygame.transform.scale(grass, (tilesize, tilesize))

dirt = pygame.image.load("Tiles/grassCenter.png")
dirt = pygame.transform.scale(dirt, (tilesize, tilesize))

snowCliffLeft = pygame.image.load("Tiles/snowCliffLeft.png")
snowCliffLeft = pygame.transform.scale(snowCliffLeft, (tilesize, tilesize))

snowCliffRight = pygame.image.load("Tiles/snowCliffRight.png")
snowCliffRight = pygame.transform.scale(snowCliffRight, (tilesize, tilesize))

grassCliffLeft = pygame.image.load("Tiles/grassCliffLeft.png")
grassCliffLeft = pygame.transform.scale(grassCliffLeft, (tilesize, tilesize))

grassCliffRight = pygame.image.load("Tiles/grassCliffRight.png")
grassCliffRight = pygame.transform.scale(grassCliffRight, (tilesize, tilesize))

snowMid = pygame.image.load("Tiles/snowMid.png")
snowMid = pygame.transform.scale(snowMid, (tilesize, tilesize))

paused = False
playerWidth = 32
playerHeight = 32
impact = 1.5
sneakHeight = 20
sneakWidth = 40
camera_offset_x = 0
camera_offset_y = 0
counter1 = 0
PPS = 3
ammo = [pygame.Rect(400+floorX,400, 15, 15),pygame.Rect(400+floorX,50, 15, 15), pygame.Rect(400+floorX,300, 15, 15)]
game = True

dash = False
while game:
    color = (0,0,0)
    dashCounter += 1
    if dashCounter<60:
        dash = False
    if dashCounter > 60:
        color = (0,255,0)
    tileRects = []
    player = pygame.Rect(x, y , playerWidth, playerHeight)
    direction = rightVelocity -leftVelocity

    if x-floorX > score:
        score = int(x-floorX)
    for i in range(0,int(x/20)-5):
        if map2[i][len(map2[i])-1] == '1':
            map2[i].append(f"{random.randint(-2,2)}")
        if map2[i][len(map2[i])-1] == '4':
            generate = random.randint(4,5)
            map2[i].append(f"{generate}")
        if map2[i][len(map2[i])-1] == '5':
            map2[i].append(f"0")
        if map2[i][len(map2[i])-1] == '3':
            generate = random.randint(4, 5)
            map2[i].append(f"{generate}")
        if map2[i][len(map2[i])-1] == '0':
            map2[i].append(f"{random.randint(-20,3)}")
        elif map2[i][len(map2[i])-1] == '2':
            map2[i].append(f"{random.randint(0,2)}")
        else:
            map2[i].append(f"{random.randint(-20,3)}")
        
            

    for i in range(0, len(ammo)):
        if ammo[i]!=0:
            ammo[i].left = 400+floorX

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()         

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.set_cursor((12,12), smallCursor)
            if pauseRect.collidepoint(pygame.mouse.get_pos()):
                paused = True
                color = white
            
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.mouse.set_cursor((12,12),cursor)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f and dashCounter > 60:
                dash = True
                dashCounter = 0
            if event.key == pygame.K_UP and jumping == False or event.key == pygame.K_SPACE and jumping == False  or event.key == pygame.K_w and jumping == False:
                doubleCount2 += 1
                y_Velocity -= jumpHeight
                jumping = True
                jumpSoundPlaying = False
                swhooshSound.play()
            if event.key == pygame.K_UP and y_Velocity >-1.5 and falling == True and doubleJump and doubleCount2 == 0 or event.key == pygame.K_SPACE and y_Velocity >-1.5 and falling == True and doubleJump and doubleCount2 == 0 or event.key == pygame.K_w and y_Velocity >-1.5 and falling == True and doubleJump and doubleCount2 == 0:
                    y_Velocity-= jumpHeight
                    falling = False
                    doubleJump = False
                    swhooshSound.play()
            if event.key == pygame.K_DOWN or event.key == pygame.K_LSHIFT:
                playerHeight = sneakHeight
                playerWidth = sneakWidth
                maxSpeed = 1.5
                jumpHeight = 5
                knockback = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w:
                falling = True
                doubleCount2 = 0
                if doubleJump == False:
                    doubleCount += 1
                    if doubleCount == 40:
                        doubleJump = True
                        doubleCount = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_LSHIFT:
                playerHeight = 32
                playerWidth = 32
                maxSpeed = 4
                jumpHeight = 8
                knockback = 2
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                leftVelocity = 0
                left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                rightVelocity = 0
                right = False
        # if keys[pygame.K_UP] and y_Velocity >-3 and falling:
        #     falling = False
        #     y_Velocity -= jumpHeight
        if keys[pygame.K_ESCAPE] and paused == False:
                paused = True
    if paused == True and keys[pygame.K_SPACE]:
            paused = False
            color = black
            pygame.mouse.set_cursor((12,12), cursor)
            pygame.mixer_music.unpause()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            left = True
            if leftVelocity < maxSpeed:
                leftVelocity += acceleration
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            right = True
            if rightVelocity < maxSpeed:
                    rightVelocity += acceleration

    if keys[pygame.K_s] and shoot == False:
            shoot = True
    if mouse[0] and shoot == False:
            shoot = True
            
            
    if y > 500:
        failSound = pygame.mixer.Sound("invalid.mp3")
        failSound.set_volume(0.5)
        failSound.play()
        for i in range(0, 100):
            window.blit(pygame.transform.scale(logo , (logoX, logoY)), (logo_x, logo_y))
            logoX *= 1.016
            logoY *= 1.016
            pygame.display.flip()
            window.fill(white)
        pygame.mixer.music.load("20 - Game Over - Yuzo Koshiro.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()
        
        logoY += 20
        for i in range(0, 270):
            window.blit(pygame.transform.scale(logo , (logoX, logoY)), (logo_x, logo_y))
            logo_x -= 13
            pygame.display.flip()
            window.fill(white)
                
        logo_x += 1755*2
        pygame.mixer.music.fadeout(2000)
            
        for i in range(0, 100):
            window.blit(pygame.transform.scale(logo , (logoX, logoY)), (logo_x, logo_y))
            logoX *= 0.984
            logoY *= 0.984
            pygame.display.flip()
            window.fill(white)
        import Restart
        Restart()
        game = False
            
    # if y_Velocity != 0:
    #     if collision != False:
    #         y = collision.top - playerHeight
    #         y_Velocity = 0
    #         collision = False
    if shoot and Ammo>0:
        bulletCounter += 1
        if bulletCounter == bulletDelay:
            impact *=-1
            pygame.display.flip()
            Ammo -= 1
            shootSound.play()
            mouse_pos = pygame.mouse.get_pos()
            angle = math.atan2(mouse_pos[1]/2 - y, mouse_pos[0]/2 - x)
            bulletVelocity = [bulletSpeed * math.cos(angle), bulletSpeed * math.sin(angle)]
            bullets.append([x, y, bulletVelocity])
            bulletCounter = 0
            if angle < 1.5 and angle > -1.5:
                x-= knockback
                floorX += knockback/2
            else: 
                x+= knockback
                floorX -= knockback/2      
        shoot = False
        
    # for i in range(0, len(floor)):
    #     if player.bottom != floor[i].top:
    #         collision = False
    #     if player.bottom == floor[i].top:
    #         collision = True
    #         y = floor[i].top -playerHeight
    #         y_Velocity = 0
    #         if collision and jumping:
    #             y_Velocity -= jumpHeight
    
    
    # if leftVelocity != 0:
    #     if collision != False:
    #         if x >= collision.right:
    #             leftVelocity = 0
    #             collision = False
    
    # for i in range(0, len(floor)):
    #     if player.colliderect(floor[i]):
    #         if direction >0 and player.bottom >floor[i].bottom:
    #             x = floor[i].left - playerWidth
    #             leftVelocity = 0
    #         elif direction <0 and player.bottom >floor[i].bottom:
    #             x = floor[i].right
    #         if y_Velocity >0:
    #             y = floor[i].top +1-playerHeight
    #         y_Velocity = 0
    #         jumping = False
    #         doubleJump = True
    #         if jumpSoundPlaying == False:
    #             jumpSound.play()
    #             jumpSoundPlaying = True
    
    # for i in range(0, len(stickyFloor)):
    #     if player.colliderect(stickyFloor[i]):
    #         y_Velocity = 0
    #         jumping = False
    #         doubleJump = True
    #         if jumpSoundPlaying == False:
    #             jumpSound.play()
    #             jumpSoundPlaying = True
            
    # for i in range(0, len(stickyFloor)):
    #     if player.colliderect(stickyFloor[i]):
    #         y = stickyFloor[i].top -playerHeight
    #         y_Velocity = 0
    #         jumping = False
    #         if jumpSoundPlaying == False:
    #             jumpSound.play()
    #             jumpSoundPlaying = True


    for i in range(0, len(ammo)):
        if ammo[i]!=0:
            if player.colliderect(ammo[i]):
                hitSound.play()
                Ammo += 20
                ammo[i] = 0
    smallWindow.fill(white)
    # for tile in range(0, 10):
    #     pygame.draw.rect(smallWindow, (0, 0, 255), pygame.Rect(tile*50+floorX, 0, 50, 50))
    #     pygame.draw.rect(smallWindow, (0, 0, 255), pygame.Rect(50+floorX, tile*50, 50, 50))

    #     tileRects.append(pygame.Rect(tile*50, 50, 50, 50))

    y1 = 0
    for row in map1:
        x1 = 0
        for tile in row:
            if tile == '1':
                smallWindow.blit(dirt, (x1*tilesize+floorX,y1*tilesize))
            elif tile == '2':
                smallWindow.blit(grass, (x1*tilesize+floorX,y1*tilesize))
            elif tile == '3':
                smallWindow.blit(snowCliffLeft, (x1*tilesize+floorX,y1*tilesize))
            elif tile == '4':
                smallWindow.blit(snowMid, (x1*tilesize+floorX,y1*tilesize))
            elif tile == '5':
                smallWindow.blit(snowCliffRight, (x1*tilesize+floorX,y1*tilesize))
            elif tile == '6':
                smallWindow.blit(grassCliffRight, (x1*tilesize+floorX,y1*tilesize))
            elif tile == '7':
                smallWindow.blit(grassCliffLeft, (x1*tilesize+floorX,y1*tilesize))
            if tile == '1' or tile == '2' or tile =='3' or tile == '4' or tile == '5' or tile == '6' or tile == '7':
                tileRects.append((pygame.Rect(x1*tilesize,y1*tilesize, tilesize, tilesize)))
                tilecount += 1
            x1 += 1
        y1+= 1

    y2 = 0
    for row in map2:
        x2 = 0
        for tile in row:
            if tile == '1':
                smallWindow.blit(dirt, (x2*tilesize+floorX,y2*tilesize))
            elif tile == '2':
                smallWindow.blit(grass, (x2*tilesize+floorX,y2*tilesize))
            elif tile == '3':
                smallWindow.blit(snowCliffLeft, (x2*tilesize+floorX,y2*tilesize))
            elif tile == '4':
                smallWindow.blit(snowMid, (x2*tilesize+floorX,y2*tilesize))
            elif tile == '5':
                smallWindow.blit(snowCliffRight, (x2*tilesize+floorX,y2*tilesize))
            elif tile == '6':
                smallWindow.blit(grassCliffRight, (x2*tilesize+floorX,y2*tilesize))
            elif tile == '7':
                smallWindow.blit(grassCliffLeft, (x2*tilesize+floorX,y2*tilesize))
            if tile == '1' or tile == '2' or tile =='3' or tile == '4' or tile == '5' or tile == '6' or tile == '7':
                tileRects.append((pygame.Rect(x2*tilesize,y2*tilesize, tilesize, tilesize)))
                tilecount += 1
            x2 += 1
        y2+= 1


    y_Velocity += gravity
    y+= y_Velocity
    if y_Velocity>20:
        y_Velocity  = 20 
    
    for tile in tileRects:
        if player.colliderect(tile.move(+floorX, 0)):
            if y_Velocity >0:
                y = tile.top +1 - playerHeight
                jumping = False
                doubleJump = True
                y_Velocity = 0
                if jumpSoundPlaying == False:
                    jumpSound.play()
                    jumpSoundPlaying = True
            elif y_Velocity <0:
                player.top = tile.bottom
                


    if x > 125:
        x-= leftVelocity
    else:
        floorX += leftVelocity
    if x <375:
        x+= rightVelocity
    else:
        floorX -= rightVelocity
        
    for tile in tileRects:
        if player.colliderect(tile):
            if direction >0:
                player.right = tile.left
                leftVelocity = 0
            elif direction <0:
                player.left = tile.right
                rightVelocity = 0

    player = pygame.Rect(x, y , playerWidth, playerHeight)
    # if left and right:
    #     playerImage = smallWindow.blit((pygame.image.load("player2/playeranim000"+ str(frame)+ ".png")), player)
    # if not left and not right and last == True:
    #     playerImage = smallWindow.blit((pygame.image.load("player2/playeranim000"+ str(frame)+ ".png")), player)
    # if not left and not right and last == False:
    #     playerImage = smallWindow.blit((pygame.image.load("player/playeranim000"+ str(frame)+ ".png")), player)
    # if left and not right:
    #     smallWindow.blit((pygame.image.load("player2/playeranim000"+ str(frame)+ ".png")), player)
    #     playerImage = smallWindow.blit((pygame.image.load("player2/playeranim000"+ str(frame)+ ".png")), player)
    #     last = True
    # if right and not left:
    #     smallWindow.blit((pygame.image.load("player/playeranim000"+ str(frame)+ ".png")), player)
    #     playerImage = smallWindow.blit((pygame.image.load("player/playeranim000"+ str(frame)+ ".png")), player)
    #     last = False
    # counter += 1
    # if left and not right and counter >PPS:
    #     smallWindow.blit((pygame.image.load("player2/playeranim000"+ str(frame)+ ".png")), player)
    #     if frame < 8:
    #         frame += 1
    #     else:
    #         frame = 0
    #     counter = 0
    # if right and not left and counter >PPS:
    #     smallWindow.blit((pygame.image.load("player/playeranim000"+ str(frame)+ ".png")), player)
    #     if frame < 8:
    #         frame += 1
    #     else:
    #         frame = 0
    #     counter = 0
    for bullet in bullets:
        isRemoved = False
        bullet[0] += bullet[2][0]
        bullet[1] += bullet[2][1]

    for bullet in bullets:
        if bullet != 0:
            pygame.draw.circle(smallWindow, black, (int(bullet[0]), int(bullet[1])), bulletRadius)
    bulletAmount = len(bullets)
    # for bullet in bullets:
    #     for i in range(0, len(tileRects)):
    #         if tilere[i].collidepoint(bullet[0], bullet[1]):
    #             pygame.draw.circle(smallWindow, red, (20, 250), 15)
    #             bullets.pop(i)
    #             hitCount += 1
    #             hitSound.play()
    for count in range(0, len(bullets)):
        for i in range(0, len(ammo)):
            if ammo[i]!= 0 and ammo[i].collidepoint(bullet[0], bullet[1]):
                bullets.pop(count)
                hitSound.play()
                Ammo += 20
                ammo[i] = 0
    for bullet in bullets:
        for i in range(0, len(tileRects)):
            if bullet != 0 and tileRects[i].collidepoint(bullet[0], bullet[1]) and not isRemoved:
                print("hit")
                bullets.remove(bullet)
                hitSound.play()
                poof = smallWindow.blit(pygame.transform.scale((pygame.image.load("poof.png")),(12,12)), (bullet[0],bullet[1]))
                isRemoved = True
    
    if left and y_Velocity <=0:
        smallWindow.blit(walkLeft.subsurface(walkCurrent,0, 32,32), player)
        frame += 1
        if frame == 5:
            walkCurrent += 32
            frame = 0
        if walkCurrent == 192:
            walkCurrent = 0
    if right and not left and y_Velocity <=0:
        smallWindow.blit(walkRight.subsurface(walkCurrent,0, 32,32), player)
        frame += 1
        if frame == 5:
            walkCurrent += 32
            frame = 0
        if walkCurrent == 192:
            walkCurrent = 0
    if not left and not right and y_Velocity <=0:
        smallWindow.blit(walk.subsurface(walkCurrent,0, 32,32), player)
        frame += 1
        if frame == 5:
            walkCurrent += 32
            frame = 0
        if walkCurrent == 192:
            walkCurrent = 0
    if y_Velocity > 0:
        smallWindow.blit(roll.subsurface(walkCurrent,0, 32,64), player)
        frame += 1
        if frame == 5:
            walkCurrent += 32
            frame = 0
        if walkCurrent == 192:
            walkCurrent = 0
    if dash:
        if pygame.mouse.get_pos()[0]/2 > x:
            x += 50
        elif pygame.mouse.get_pos()[0]/2 < x:
            x -= 50
        if pygame.mouse.get_pos()[0]/2 > y:
            y -= 50
        elif pygame.mouse.get_pos()[0]/2 < y:
            y -= 50
    scoreRect.topright = (x + 45, y - 15 - impact/2)
    scoreText = font.render("Score: " + str(score), True, black)
    smallWindow.blit(scoreText, scoreRect)
    for i in range(0, len(ammo)):
        if ammo[i] != 0:
            smallWindow.blit(ammoImg, ammo[i])
    ammoText = font.render(f"Ammo :  {Ammo}", True, black)
    smallWindow.blit(ammoText, ammoRect)
    pauseText = font.render("Pause", True, color)
    if paused == True:
        smallWindow.fill(black)
        smallWindow.blit(pausedText, pausedRect)
        color = white
        smallWindow.blit(pauseText, pauseRect)
        pygame.mouse.set_cursor((12, 12),cursorWhite)
        pygame.mixer.music.pause()
    smallWindow.blit(pauseText, pauseRect)
    display = pygame.transform.scale(smallWindow, (width, height))
    window.blit(display, (0,0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()