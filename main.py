import math
import os
import random

import pygame
from pygame import mixer

WIDTH, HEIGHT = 800, 600

pygame.init()

#create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#title and icon
pygame.display.set_caption("Space Invadors")
iconPath = os.path.join('assets','icon.png')
icon = pygame.image.load(iconPath)
bgImgPath = os.path.join('assets', 'background.png')
bgImg = pygame.image.load(bgImgPath)
pygame.display.set_icon(icon)

#audio
#background
backgroundPath = os.path.join('assets', 'sounds', 'background.mp3')
mixer.music.load(backgroundPath)
mixer.music.set_volume(0.2)
mixer.music.play(-1) #-1 means play on loop

#shoot
shootSoundPath = os.path.join('assets', 'sounds', 'laser.mp3')
shootSound = mixer.Sound(shootSoundPath)
shootSound.set_volume(1)

#blast enemy
enemyBlastSoundPath = os.path.join('assets', 'sounds', 'pop.mp3')
enemyBlastSound = mixer.Sound(enemyBlastSoundPath)
enemyBlastSound.set_volume(0.5)

#enemy hits player
blastSoundPath = os.path.join('assets', 'sounds', 'explode.mp3')
blastSound = mixer.Sound(blastSoundPath)
blastSound.set_volume(1)

#player
playerImgPath = os.path.join('assets', 'player-ship.png')
playerImg = pygame.image.load(playerImgPath)
playerX, playerY = 370, HEIGHT-100
playerXOffset = 3.5

def player(x,y):
    screen.blit(playerImg, (x, y))
    #blit method draws the image

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyXChange = []
numOfEnemies = 16
enemyXOffset = 2.5
enemyYOffset = 35
enemyImgPath = os.path.join('assets', 'enemy.png')

for i in range(numOfEnemies):
    enemyImg.append(pygame.image.load(enemyImgPath))
    enemyX.append(random.randint(20,WIDTH-85))
    enemyY.append(random.randint(50,250))
    enemyXChange.append(enemyXOffset)

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))


#bullet
bulletImgPath = os.path.join('assets', 'bullet.png')
bulletImg = pygame.image.load(bulletImgPath)
bulletX = playerX
bulletY = playerY
bulletYOffset = 17
bulletState = "ready" #ready - we can't see on the screen, fire - we can see on the screen
    
def fireBullet(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x+16, y+10))

#collision
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX),2) + math.pow((enemyY-bulletY),2))
    if distance < 27:
        return True
    return False

#gameover logic
def isGameOver(playerX, playerY, enemyX, enemyY):
    if (enemyY >= playerY-64) and (playerX-64 <= enemyX <= playerX+64):
        return True
#game over text
fontPath = os.path.join('assets', 'fonts', 'Korcy.ttf')
gameOverFont = pygame.font.Font(fontPath, 72)
def showGameOverText(x,y):
    gameOverText = gameOverFont.render("Game Over", True, (255,255,0))
    scoreText = gameOverFont.render("Score: " + str(scoreValue), True, (255,255,0))

    screen.blit(scoreText, (x-50,y))
    screen.blit(gameOverText, (x-100,y+100))
    
#score
scoreValue = 0
scoreFont = pygame.font.Font(fontPath, 32) #32 is the size
textX, textY = 10, 10

def showScore(x,y):
    score = scoreFont.render("Score: " + str(scoreValue), True, (255,255,255))
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
                    shootSound.play()
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
            enemyBlastSound.play()
            bulletY = playerY
            enemyX[i] = random.randint(20,WIDTH-85)
            enemyY[i] = random.randint(50, 100)
            enemy(enemyX[i], enemyY[i], i)
            bulletState = "ready"
            scoreValue += 1
        
        if isGameOver(playerX, playerY, enemyX[i], enemyY[i]):
            for j in range(numOfEnemies):
                blastSound.play()
                running = False

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

running = True
while running:
    screen.blit(bgImg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    showGameOverText(WIDTH/2-100, HEIGHT/2-100)

    pygame.display.update()