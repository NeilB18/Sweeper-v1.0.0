from math import *
import pygame



pygame.init()
screen = pygame.display.set_mode((1000,600))
def draw(name,x,y):
    screen.blit(name,(x,y))


def check_collision(object_radius,x1,y1,x2,y2):
    
    d = sqrt((pow(x2-x1 ,2))+(pow(y2-y1,2)))
    if d < object_radius :
        return True

    else: 
        return False

def find_duplicates():
    duplicates= tuple()

    



    
