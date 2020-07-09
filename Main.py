import pygame
import sys
import math
import random

#Init & Settings
pygame.init()

screen = pygame.display.set_mode((800,600))
icon = pygame.image.load('F5S4.png')
pygame.display.set_caption("SpaceWars")
pygame.display.set_icon(icon)
bg = pygame.image.load('galaxy2.jpg')
shipSound = pygame.mixer.Sound('shipSound.wav')

#Player
playerImg = pygame.image.load('F5S4.png')
playerImg = pygame.transform.scale(playerImg,(50,50))
playerX = 100
playerY = 100
playerXChange = 0
playerYChange = 0
playerRotation = 0
score = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

#Enemy
enemyImg = pygame.image.load('fighter.png')
enemyImg = pygame.transform.scale(enemyImg,(50,50))

EnemyX = random.randint(0,800)
EnemyY = random.randint(50,150)

EnemyXchange = 1
EnemyYchange = 1

def Enemy(x,y):
    screen.blit(enemyImg,(x,y))


#Laser Beam
laserImg =  pygame.image.load('laser.png')
laserImg = pygame.transform.scale(laserImg,(25,25))
laserX = 0
laserY = 0
laserChangeY = 1
laserChangeX = 0
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(laserImg,(x+16,y+10))


def isCollision(enemyX,enemyY,laserX,laserY):
    distance = math.sqrt(math.pow(enemyX-laserX,2)+ math.pow(enemyY-laserY,2))
    if distance <27:
        return True
    else:
        return False



#Game
running = True
while running :
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
         running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange = -1

            if event.key == pygame.K_RIGHT:
                playerXChange = 1
            if event.key == pygame.K_UP:
                playerYChange = -1
                #shipSound.play()
            if event.key == pygame.K_DOWN:
                playerYChange = 1
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,playerY)

        if event.type == pygame.KEYUP:
            playerXChange = 0
            playerYChange = 0

    playerX += playerXChange
    playerY += playerYChange
    #EnemyX += EnemyXchange
    #EnemyY += EnemyYchange


    #laser movement
    if bullet_state is "fire":
        fire_bullet(playerX,laserY)
        laserY -= laserChangeY


#collision
    collision = isCollision(EnemyX,EnemyY,laserX,laserY)
    if collision:
        laserY = 600
        bullet_state = "ready"
        score += 1
        print("score is:" + score)



    if playerX <= 0:
        playerX =800
    elif playerX >=800:
        playerX = 0
    if playerY <= 0:
        playerY = 600
    elif playerY >= 600:
        playerY = 0



    if EnemyX <= 0:
        EnemyXchange = 1
    elif EnemyX >= 800:
        EnemyXchange = -1
    if EnemyY <= 0:
       EnemyYchange = 1
    elif EnemyY >= 600:
        EnemyYchange = -1

    if laserY <= 0:
        bullet_state = "ready"
    elif laserY >= 800:
        bullet_state = "ready"




    player(playerX,playerY)
    Enemy(EnemyX,EnemyY)
    pygame.display.update()



