import pygame, asyncio
import sys
from pygame.locals import QUIT
import random
import os
import time

pygame.init()
pygame.display.set_caption("A ball chasing love")
sw=400
sh=300
screen = pygame.display.set_mode((sw,sh))
clock = pygame.time.Clock()
BLACK= (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (192,192,192)
YELLOW = (255, 255, 0)

done=False
score=0


heart=pygame.image.load("heart.png")
heart=pygame.transform.scale(heart,(17,17))
rect=heart.get_rect()
speed = [2,5]
circle=pygame.image.load("circle.png")
circle=pygame.transform.scale(circle,(77,60))
c_rect=circle.get_rect()
c_rect.x=round(20)
c_rect.y=round(20)
x=20
y=20
hx=200
hy=200
font=pygame.font.Font(None,30)

    
async def main():
    global done
    global score
    global rect
    while not done:
        clock.tick(60)
        SCORE=font.render("SCORE : {}/1000".format(score),True, (WHITE))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
                break

        if rect.colliderect(c_rect):
            score=score+1
        if score==100:
            done=True
            break

        rect = rect.move(speed)
        if rect.left<0 or rect.right>sw:
            speed[0] = -speed[0]
        if rect.top<0 or rect.bottom>sh:
            speed[1] = -speed[1]
                
        key_event = pygame.key.get_pressed()
        if key_event[pygame.K_LEFT]:
            c_rect.x-=5
        if key_event[pygame.K_RIGHT]:
            c_rect.x+=5
        if key_event[pygame.K_UP]:
            c_rect.y-=5
        if key_event[pygame.K_DOWN]:
            c_rect.y+=5
        if c_rect.x>350:
            c_rect.x=350
        if c_rect.x<-15:
            c_rect.x=-15
        if c_rect.y>250:
            c_rect.y=250
        if c_rect.y<-10:
            c_rect.y=-10

        screen.fill(BLACK)
        screen.blit(heart, rect)
        screen.blit(circle, c_rect)
        screen.blit(SCORE, (200,0))
        pygame.display.update()
        await asyncio.sleep(0)
    pygame.quit()
asyncio.run(main())



