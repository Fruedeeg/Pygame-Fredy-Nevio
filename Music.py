import pygame
pygame.display.set_caption("Music")
pygame.init()
musicList = ["01 - Player Select V2 - Yuzo Koshiro.mp3", "02 - Go Straight - Yuzo Koshiro.mp3","03 - In the Bar - Yuzo Koshiro.mp3","04 - Never Return Alive - Yuzo Koshiro.mp3","05 - Spin on the Bridge - Yuzo Koshiro.mp3", "06 - Ready Funk - Yuzo Koshiro.mp3","07 - Dreamer - Yuzo Koshiro.mp3","08 - Alien Power - Yuzo Koshiro.mp3","10 - Too Deep - Yuzo Koshiro.mp3","11 - Slow Moon - Yuzo Koshiro.mp3","12 - Wave 131 - Yuzo Koshiro.mp3","13 - Jungle Base - Motohiro Kawashima, Yuzo Koshiro.mp3","14 - Back to the Industry - Yuzo Koshiro.mp3","15 - Expander - Motohiro Kawashima.mp3","16 - SOR Super Mix - Yuzo Koshiro.mp3","17 - Max Man - Motohiro Kawashima.mp3","18 - Revenge of Mr. X - Yuzo Koshiro.mp3","19 - Good Ending - Yuzo Koshiro.mp3","20 - Game Over - Yuzo Koshiro.mp3","21 - Go Straight (Beatmix) - Yuzo Koshiro.mp3","22 - Beta - Walking Bottom - Yuzo Koshiro.mp3","23 - Little Money Avenue - Motohiro Kawashima.mp3"]

font = pygame.font.SysFont('Liberation Sans', 20)
font2 = pygame.font.SysFont('Liberation Sans', 15)

coverImage = pygame.image.load("streetsOfRage.jpg")
width = 1000
height = 1000
window = pygame.display.set_mode((width, height))
playing = False
rectList = []
pygame.mixer.Sound("15 - Expander - Motohiro Kawashima.mp3").play()
currentMusic = "15 - Expander - Motohiro Kawashima"
music = True

while music:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            music = False
    window.fill((255,255,255))
    for i in range(0,11):
        pygame.draw.rect(window, (0,0,0), pygame.Rect(width // 2 - 425, 500 +45*i, 400, 35))
        rectList.append(pygame.Rect(width // 2 - 425, 500 +45*i, 400, 35))
        text = font2.render(musicList[i], True, (255,255,255))
        window.blit(text, rectList[i])
    for i in range(0,11):
        pygame.draw.rect(window, (0,0,0), pygame.Rect(width // 2 + 25, 500 +45*i, 400, 35))
        rectList.append(pygame.Rect(width // 2 + 25, 500 +45*i, 400, 35))
        text = font2.render(musicList[i+11], True, (255,255,255))
        window.blit(text, rectList[i+11])
    for rect in rectList:
        if rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, (100,100,100), rect)
            i = rectList.index(rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if playing == False:
            pygame.mixer.stop()
            pygame.mixer.Sound(musicList[i]).play()
            currentMusic = musicList[i]
        if (pygame.Rect(525, 75, 400, 50)).collidepoint(pygame.mouse.get_pos()):
            import Menu
            Menu()
    if event.type == pygame.MOUSEBUTTONUP:
        playing == False
    coverImage = pygame.transform.scale(coverImage, (400,400))
    image = pygame.Rect(75, 75, 200, 200)
    imageRight = pygame.Rect(525, 450, 200, 200)
    text = font.render(currentMusic, True, (0,0,0))
    text_rect = text.get_rect()
    window.blit(text, imageRight)
    text = font.render("Back to Menu", True, (255,255,255))
    backToMenu = pygame.Rect(550, 85, 400, 50)
    pygame.draw.rect(window, (0,0,0), pygame.Rect(525, 75, 400, 50))
    window.blit(text, backToMenu)
    window.blit(coverImage, image)
    pygame.display.update()
pygame.quit()