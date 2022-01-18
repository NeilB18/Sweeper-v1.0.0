from math import *
import pygame

from Menu import check_if_clicked


pygame.init()
screen = pygame.display.set_mode((1000,600))
def draw(name,x,y):
    screen.blit(name,(x,y))

# def text_input():
#     while RuntimeWarning
#     mouse_x,mouse_y = pygame.mouse.get_pos()
#     if check_if_clicked():
#         print("")

def check_collision(object_radius,x1,y1,x2,y2):
    
    d = sqrt((pow(x2-x1 ,2))+(pow(y2-y1,2)))
    if d < object_radius :
        return True

    else: 
        return False

def find_duplicates():
    duplicates= tuple()

    



    
