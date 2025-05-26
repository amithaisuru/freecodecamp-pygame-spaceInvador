import pygame

WIDTH, HEIGHT = 800, 600

pygame.init()

#create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#title and icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('assets/player-ship.png')
playerX, playerY = 370, 480

def player():
    screen.blit(playerImg, (playerX, playerY))
    #blit method draws the image

#game loop
running = True
while running:
     #screen fill
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    player()

    pygame.display.update()