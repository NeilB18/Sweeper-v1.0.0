import pygame
import sys
from random import randint as rt
import Buttons
from pygame import mixer
pygame.init()
mixer.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_icon(pygame.image.load("Assets/images/icon_1.png"))
pygame.display.set_caption("Sweeper")
mouse_click = False
def check_if_clicked():
    global mouse_click
    if mouse_click == True:
        return True
    else:
        return False

def close_menu():
    global running_1
    running_1 = False

def run_menu():
    global mouse_click,running,screen
    running_1 = True        
    dot_x_list = []
    dot_y_list = []
    dot_color_list = []
    dot_radius_list = []
    dot_vel_list = []
    running = False
    start_button = pygame.image.load("Assets/images/start_button.png")
    start_button_2 = pygame.image.load("Assets/images/start_button_2.png")

    exit_button = pygame.image.load("Assets/images/Exit_1.png")
    exit_button.set_colorkey((0,0,0))
    fullscreen = False

    for i in range(1000):
        dot_color_list.append((rt(0,250),rt(0,250),rt(0,250)))
        dot_x_list.append(rt(0,1000))
        dot_y_list.append(rt(0,600))
        dot_radius_list.append(rt(2,6))
        dot_vel_list.append(rt(1,3))


    button_1 = pygame.Rect(400,275,200,50)
    button_2 = pygame.Rect(400,335,220,50)

    mixer.music.load("Menu_music_1.mp3")

    mixer.music.play(-1,0.0)

    while running_1:
        
        
        mouse_x,mouse_y = pygame.mouse.get_pos()
        screen.fill((255,255,255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_1 = False
                running = True
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            
            if running == True:
                mixer.music.stop()
            


 

        for j in range(1000):
            dot_y_list[j]+=dot_vel_list[j]

         

            if dot_y_list[j]>=600:
                dot_y_list[j] =-dot_vel_list[j]
            pygame.draw.circle(screen,dot_color_list[j],(dot_x_list[j],dot_y_list[j]),dot_radius_list[j])


        
        screen.blit(start_button,(400,275))
        screen.blit(exit_button,(400,335))


        if button_1.collidepoint((mouse_x,mouse_y)):
            screen.blit(start_button_2,(400,275))

            if check_if_clicked():
                click_sound = mixer.Sound('click.wav')
                click_sound.play()
                running_1 = False
        if button_2.collidepoint((mouse_x,mouse_y)):
            screen.blit(exit_button,(400,335))

            
            if check_if_clicked():
                click_sound = mixer.Sound('click.wav')
                click_sound.play()
                
                
                sys.exit()
        # screen.blit(option,(510,275))
        # 
        
       


        pygame.display.update()

if __name__ == "__main__":
    run_menu()