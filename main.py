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
enemyImg = []
enemyX = []
enemyY = []
enemyXChange = []
numOfEnemies = 10
enemyXOffset = 1.5
enemyYOffset = 30

for i in range(numOfEnemies):
    enemyImg.append(pygame.image.load('assets/enemy.png'))
    enemyX.append(random.randint(20,WIDTH-85))
    enemyY.append(random.randint(50,100))
    enemyXChange.append(enemyXOffset)

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))


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

#score
scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 32) #32 is the size
textX, textY = 10, 10

def showScore(x,y):
    score = font.render("Score: " + str(scoreValue), True, (255,255,255))
    screen.blit(score, (x,y))

#game loop
playerXChange = 0 #pixels
running = True
while running:
     #screen fill
    screen.fill((0,0,0))
    #background image
    screen.blit(bgImg,(0,0))
    #score
    showScore(textX, textY)

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
                if bulletState == "ready":
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
    for i in range(numOfEnemies):
        enemyX[i] += enemyXChange[i]
        #check enemy boundary
        if enemyX[i] < 0:
            enemyXChange[i] = enemyXOffset
            enemyY[i]+=enemyYOffset
        if enemyX[i]+64 > WIDTH: #64 is player image width
            enemyXChange[i] = -enemyXOffset
            enemyY[i]+=enemyYOffset

        #bullet collision with enemy
        if isCollision(bulletX, bulletY, enemyX[i], enemyY[i]):
            bulletY = playerY
            enemyX[i] = random.randint(20,WIDTH-85)
            enemyY[i] = random.randint(50, 100)
            enemy(enemyX[i], enemyY[i], i)
            bulletState = "ready"
            scoreValue += 1

        enemy(enemyX[i], enemyY[i], i)

    #bullet
    if bulletState == "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletYOffset
    #bullet reset
    if bulletY<=0:
        bulletY = playerY
        bulletState = "ready"
    

    pygame.display.update()