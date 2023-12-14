import pygame
import random
import math
from pygame import mixer

pygame.init()
screen= pygame.display.set_mode((800,600))
background=pygame.image.load('spacer.png')
mixer.music.load('background.wav')
mixer.music.play(-1)
pygame.display.set_caption("This my game")
icon=pygame.image.load('game-console.png')
pygame.display.set_icon(icon)
playerimg=pygame.image.load('spaceship.png')
playerx=370
playery=480
playerchangex=0
enemyimg=[]
enemyx=[]
enemyy=[]
enemychangex=[]
enemychangey=[]
numofenemy=6

for i in range(numofenemy):
    enemyimg.append(pygame.image.load('ghoster.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,150))
    enemychangex.append(4)
    enemychangey.append(40)


bulletimg=pygame.image.load('bullet.png')
bulletx=0
bullety=480
bulletstate="ready"
bulletchangey=10
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
overfont=pygame.font.Font('freesansbold.ttf',64)
textx= 10
texty=10

def showscore(x,y):
    score=font.render("Score:"+str(score_value),True, (255,255,255))
    screen.blit(score,(x,y))
def gameover():
    gameend=overfont.render("GAME OVER",True, (255,255,255))
    screen.blit(gameend , (200,250))

def fire_bullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimg,(x+16,y+10))

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def collision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2)))
    if distance < 30:
        return True
    else:
        return False
    
running= True
while running:
    screen.fill((44,44,62))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                playerchangex =-5
            elif event.key== pygame.K_RIGHT:
                playerchangex =5
            elif event.key== pygame.K_SPACE:
                if bulletstate=="ready":
                    bulletsound=mixer.Sound('laser.wav')
                    bulletsound.play()
                    bulletx=playerx
                    fire_bullet(bulletx,bullety)
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerchangex=0
                    
    playerx +=playerchangex
    if playerx <=0:
        playerx=0
    elif playerx >=736:
        playerx=736
    for i in range(numofenemy):
        if enemyy[i]>440:
            for j in range(numofenemy):
                enemyy[j]=2000
            gameover()
            break

        enemyx[i] +=enemychangex[i]
        if enemyx[i] <=0:
            enemychangex[i]=3
            enemyy[i]+=enemychangey[i]
        elif enemyx[i] >=736:
            enemychangex[i]=-3
            enemyy[i]+=enemychangey[i]

        iscollision=collision(enemyx[i],enemyy[i],bulletx,bullety)
        if iscollision:
            collidesound=mixer.Sound('explosion.wav')
            collidesound.play()
            bullety=480
            bulletstate="ready"
            score_value+=1
            
            enemyx[i]=random.randint(0,735)
            enemyy[i]=random.randint(50,150)
        enemy(enemyx[i],enemyy[i],i)

    if bulletstate == "fire":
        fire_bullet(bulletx,bullety)
        bullety -=bulletchangey
    if bullety <=0:
        bullety=480
        bulletstate="ready"
    
    

    player(playerx,playery)
    showscore(textx,texty)
    pygame.display.update()
    
