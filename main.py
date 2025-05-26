import math
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


#bullet
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = playerX
bulletY = playerY
bulletYOffset = 10
bulletState = "ready" #ready - we can't see on the screen, fire - we can see on the screen
    
def fireBullet(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x+16, y+10))

#collidion
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX),2) + math.pow((enemyY-bulletY),2))
    if distance < 27:
        return True
    return False

playerXChange = 0 #pixels
enemyXChange = enemyXOffset #pixels
score = 0
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
            if event.key == pygame.K_SPACE:
                if bulletState is "ready":
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)
        if event.type == pygame.KEYUP: #is a key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXChange = 0

    #player
    playerX += playerXChange
    #check player boundary
    if playerX < 0:
        playerXChange = 0
    if playerX+64 > WIDTH: #64 is player image width
        playerXChange = 0 
    player(playerX, playerY)

    #enemy
    enemyX += enemyXChange
    #check enemy boundary
    if enemyX < 0:
        enemyXChange = enemyXOffset
        enemyY+=enemyYOffset
    if enemyX+64 > WIDTH: #64 is player image width
        enemyXChange = -enemyXOffset
        enemyY+=enemyYOffset
    enemy(enemyX, enemyY)

    #bullet
    if bulletState is "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletYOffset
    #bullet reset
    if bulletY<=0:
        bulletY = playerY
        bulletState = "ready"
    
    #bullet collision with enemy
    if isCollision(bulletX, bulletY, enemyX, enemyY):
        bulletY = playerY
        bulletState = "ready"
        score += 1
        print(score)

    pygame.display.update()