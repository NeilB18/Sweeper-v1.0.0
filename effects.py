from typing import Tuple
import pygame
import sys
from random import randint as rt

pygame.init()

particles = []

def make_particle(screen,x,y,color):
    global particles 
    particles.append([[x,y], 
                 [rt(0,20)/10 - 1,-2],
                 rt(4,6)])
    
    for particle in particles:
        particle[0][0] -= particle[1][0]
        particle[0][1] -= particle[1][1]
        particle[2]-=0.1
        particle[1][1] -= 0.09
        pygame.draw.circle(screen,color,[int(particle[0][0]),int(particle[0][1])], int(particle[2]))

        if particle[2]<=0:
            particles.remove(particle)