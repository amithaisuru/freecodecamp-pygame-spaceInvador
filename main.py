import random

import pygame

WIDTH, HEIGHT = 800, 600

pygame.init()

#create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#title and icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load('assets/icon.png')
bgImg = pygame.image.load('assets/background.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('assets/player-ship.png')
playerX, playerY = 370, HEIGHT-100
playerXOffset = 2

def player(x,y):
    screen.blit(playerImg, (x, y))
    #blit method draws the image

#enemy
enemyImg = pygame.image.load('assets/enemy.png')
enemyX = random.randint(0,WIDTH)
enemyY = random.randint(50, 150)
enemyXOffset = 1.5
enemyYOffset = 30

def enemy(x,y):
    screen.blit(enemyImg, (x,y))

playerXChange = 0 #pixels
enemyXChange = enemyXOffset #pixels
#game loop
running = True
while running:
     #screen fill
    screen.fill((0,0,0))
    #background image
    screen.blit(bgImg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # if keystroke is pressed check whether it is right or left
        if event.type == pygame.KEYDOWN: #is a key prssed
            if event.key == pygame.K_LEFT: #check if the pressd key is left arrow
                playerXChange = -playerXOffset
            if event.key == pygame.K_RIGHT:
                playerXChange = playerXOffset
        if event.type == pygame.KEYUP: #is a key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXChange = 0

    playerX += playerXChange

    #check player boundary
    if playerX < 0:
        playerXChange = 0
    if playerX+64 > WIDTH: #64 is player image width
        playerXChange = 0 
    player(playerX, playerY)

    enemyX += enemyXChange

    #check enemy boundary
    if enemyX < 0:
        enemyXChange = enemyXOffset
        enemyY+=enemyYOffset
    if enemyX+64 > WIDTH: #64 is player image width
        enemyXChange = -enemyXOffset
        enemyY+=enemyYOffset

    enemy(enemyX, enemyY)


    pygame.display.update()