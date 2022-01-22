from datetime import time
import os
import sys
import pygame
from Functions import draw
from random import choice,randrange,randint

from Functions import draw

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()


alpha_value = randrange(30,40,5)

screen = pygame.display.set_mode((1000,600))
display_surface= pygame.Surface((1000,600))

clock = pygame.time.Clock()

chars = ['~','1','2','0','+',':','^','$']


   

running = True

font = pygame.font.SysFont("segoeuisymbol",25)

vel = 40

green_chars = [font.render(char,True,(0,255,0)) for char in chars]

X_list = []
Y_list = []

code_x = randint(0,1000)
code_y = -1

for x in range(len(green_chars)):
    X_list.append(code_x)
    Y_list.append(code_y)





for x in range(randrange(30,40,5)):
    
    i = choice(green_chars)



def draw_code():
    
    for g in range(len(green_chars)):

        code = font.render(f"{str(i)}",True,(0,255,0))
        
        draw(code,code_x,code_y)

display_surface.set_alpha(alpha_value)

while running:
    i = choice(chars)
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    code_y+=vel

    if code_y >=600:
        code_y = -1
        code_x = randint(0,1000)
    
    draw_code()
  
    pygame.display.update()
    clock.tick(60)