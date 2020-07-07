import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800,600))
icon = pygame.image.load('F5S4.png')

pygame.display.set_caption("SpaceWars")
pygame.display.set_icon(icon)

bg = pygame.image.load('galaxy2.jpg')
playerImg = pygame.image.load('F5S4.png')
playerImg = pygame.transform.scale(playerImg,(50,50))
playerX = 100
playerY = 100
playerXChange = 0
playerYChange = 0
playerRotation = 0

def player(x,y):
    screen.blit(playerImg,(x,y))


running = True
while running :
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
         running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left is pressed")
                playerXChange = -0.6

            if event.key == pygame.K_RIGHT:
                print("Right is pressed")
                playerXChange = 0.6
            if event.key == pygame.K_UP:
                print("UP is pressed")
                playerYChange = -0.3
            if event.key == pygame.K_DOWN:
                print("DOWN is pressed")
                playerYChange = 0.3
            if event.key == pygame.K_SPACE:
                print("SPACEBAR is pressed")
        if event.type == pygame.KEYUP:
            print("Key has been released")
            playerXChange = 0
            playerYChange = 0

    playerX += playerXChange
    playerY += playerYChange

    if playerX <= 0:
        playerX =800
    elif playerX >=800:
        playerX = 0
    if playerY <= 0:
        playerY = 600
    elif playerY >= 600:
        playerY = 0



    player(playerX,playerY)
    pygame.display.update()


