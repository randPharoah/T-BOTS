import pygame
from pygame.locals import *
from sys import exit
import numpy as np
filename = 'pathpoints.dat'
pygame.init()
screen = pygame.display.set_mode((633, 359), 0, 0)

canvas = pygame.image.load('BestScore.png')
 
coordinate  = []

while True:
    keys = pygame.key.get_pressed()
     
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        c1, c2, c3 =  pygame.mouse.get_pressed()

        if event.type == MOUSEMOTION and c1:
            coordinate.append(event.pos)
        if c3:
            if len(coordinate)>10:
                coordinate = coordinate[0:len(coordinate)-10]
            else:
                coordinate  = []
        if keys[K_c]:
            coordinate  = []

        if keys[K_q]:
            pygame.display.quit()
            exit()
        if keys[K_s]:
            aa = np.array(coordinate)
            np.savetxt(filename,aa)   
          

    screen.blit(canvas,(0,0))
 
    if len(coordinate)>1:
        pygame.draw.lines(screen, (0,255,0), False, coordinate, 3)

    if event.type == KEYDOWN and event.key == K_ESCAPE:
        pygame.display.quit()
        exit()
      
    pygame.display.update()
