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

def player(x,y):
    screen.blit(playerImg, (x, y))
    #blit method draws the image

#game loop
running = True
while running:
     #screen fill
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # if keystroke is pressed check whether it is right or left
        if event.type == pygame.KEYDOWN: #is a key prssed
            if event.key == pygame.K_LEFT: #check if the pressd key is left arrow
                print("left pressed")
            if event.key == pygame.K_RIGHT:
                print("right pressed")
        if event.type == pygame.KEYUP: #is a key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("keys released")

    player(playerX, playerY)

    pygame.display.update()