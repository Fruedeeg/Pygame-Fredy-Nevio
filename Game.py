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

ammoImg = pygame.image.load("ammo.png") 
ammoImg = pygame.transform.scale(ammoImg, (37/1.5, 32/1.5))

pygame.mixer.music.load("02 - Go Straight - Yuzo Koshiro.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
pygame.mixer.music.play
idleframe = 0
tilecount =0

map1 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
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
        ['0','0','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','1','1','0','0','0','0','0','0','2','2','0','0','0','0','0','0','0','0',],
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




def collisionTest(rect, tiles):
    hitList = []
    for tile in tiles:
        if rect.colliderect(tile):
            hitList.append(tile)
    return hitList

def move(rect, movement, tiles):
    collision_types = {'top': False,'bottom': False,'right': False,'left': False, }
    rect.x += movement[0]
    hitList = collisionTest(rect, tiles)
    for tile in hitList:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
            
while game:
    if x-floorX > score:
        score = int(x-floorX)
    for i in range(0,int(x/20)-5):
        if map1[i][len(map1[i])-1] == '1':
            map1[i].append(f"{random.randint(-2,2)}")
        if map1[i][len(map1[i])-1] == '4':
            generate = random.randint(4,5)
            map1[i].append(f"{generate}")
        if map1[i][len(map1[i])-1] == '5':
            map1[i].append(f"0")
        if map1[i][len(map1[i])-1] == '3':
            generate = random.randint(4, 5)
            map1[i].append(f"{generate}")
        if map1[i][len(map1[i])-1] == '0':
            map1[i].append(f"{random.randint(-20,3)}")
        elif map1[i][len(map1[i])-1] == '2':
            map1[i].append(f"{random.randint(0,2)}")
        else:
            map1[i].append(f"{random.randint(-20,3)}")
        
            

    tileRects = []
    player = pygame.Rect(x, y , playerWidth, playerHeight)
    direction = rightVelocity -leftVelocity

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
    if y > 500:
        finalScore = score
        pygame.mixer.music.fadeout(500)
        pygame.mixer.music.load("21 - Game Over - Yuzo Koshiro.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()
        pygame.time.wait(5000)
        import Restart
        Restart()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and jumping == False:
            doubleCount2 += 1
            y_Velocity -= jumpHeight
            jumping = True
            jumpSoundPlaying = False
            swhooshSound.play()
        if event.key == pygame.K_UP and y_Velocity >-1.5 and falling == True and doubleJump and doubleCount2 == 0:
                y_Velocity-= jumpHeight
                falling = False
                doubleJump = False
                swhooshSound.play()
        if event.key == pygame.K_DOWN:
            playerHeight = sneakHeight
            playerWidth = sneakWidth
            maxSpeed = 1.5
            jumpHeight = 5
            knockback = 0.5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            falling = True
            doubleCount2 = 0
            if doubleJump == False:
                doubleCount += 1
                if doubleCount == 40:
                    doubleJump = True
                    doubleCount = 0
        if event.key == pygame.K_DOWN:
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
            
    # if y_Velocity != 0:
    #     if collision != False:
    #         y = collision.top - playerHeight
    #         y_Velocity = 0
    #         collision = False
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        right = True
        if rightVelocity < maxSpeed:
                rightVelocity += acceleration

    if keys[pygame.K_s] and shoot == False:
        shoot = True
    if mouse[0] and shoot == False:
        shoot = True
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
            if tile == '1' or tile == '2' or tile =='3' or tile == '4' or tile == '5':
                tileRects.append((pygame.Rect(x1*tilesize,y1*tilesize, tilesize, tilesize)))
                tilecount += 1
            x1 += 1
        y1+= 1

    y2 = 0
    for row in map2:
        x2 = 0
        for tile in row:
            if tile == '1':
                smallWindow.blit(dirt, (x2*tilesize+floorX+500,y2*tilesize))
            elif tile == '2':
                smallWindow.blit(grass, (x2*tilesize+floorX+500,y2*tilesize))
            if tile != '0':
                tileRects.append((pygame.Rect(x2*tilesize+500,y2*tilesize, tilesize, tilesize)))
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
            if bullet != 0 and tileRects[i].collidepoint(bullet[0], bullet[1]):
                print("hit")
                bullets.remove(bullet)
                hitSound.play()
    
    if left:
        smallWindow.blit(walkLeft.subsurface(walkCurrent,0, 32,32), player)
        frame += 1
        if frame == 5:
            walkCurrent += 32
            frame = 0
        if walkCurrent == 192:
            walkCurrent = 0
    if right:
        smallWindow.blit(walkRight.subsurface(walkCurrent,0, 32,32), player)
        frame += 1
        if frame == 5:
            walkCurrent += 32
            frame = 0
        if walkCurrent == 192:
            walkCurrent = 0
    if not left and not right:
        smallWindow.blit(walk.subsurface(walkCurrent,0, 32,32), player)
        frame += 1
        if frame == 5:
            walkCurrent += 32
            frame = 0
        if walkCurrent == 192:
            walkCurrent = 0


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
