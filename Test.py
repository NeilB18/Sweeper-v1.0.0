import pygame
from Menu import run_menu
from random import randint as rt
from math import *
from pygame import mixer
import sys
from Functions import *
from player import Player

from Game_AI import Enemy
import time
start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))
pygame.init()

mixer.init()



screen = pygame.display.set_mode((1000,600))
pygame.display.set_icon(pygame.image.load("Assets/images/Cleaner game icon.png"))
pygame.display.set_caption("Sweeper")
def show_text():
    
    score_P1 = font.render(f"{player_1.name}: {str(int(player_1.radius))}",True,(0,0,139))
    score_P2 = font.render(f"{player_2.name}: {str(int(player_2.radius))}",True,(139,0,0))
    
    screen.blit(score_P1,(10,10))
   
    screen.blit(score_P2,(850,10))

def show_winner(winner_name):
    game_over_text = big_font.render(f"{winner_name} Wins",winner_declared,(rt(0,230),rt(0,230),rt(0,230)))
    screen.blit(game_over_text,(1000-650,600/2-32))

def check_collision(object_radius,x1,y1,x2,y2):
    
    d = sqrt((pow(x2-x1 ,2))+(pow(y2-y1,2)))
    if d < object_radius :
        return True

    else: 
        return False
    

dot_x_list = []
dot_y_list = []
dot_list = []
dot_color_list = []
dot_vel_list = []
dot_radius_list = []
for i in range(1000):
    dot_color_list.append((rt(0,250),rt(0,250),rt(0,250)))
    dot_x_list.append(rt(0,1000))
    dot_y_list.append(rt(0,600))
    dot_vel_list.append(rt(3,6))
    dot_radius_list.append(rt(2,6))

player_vel=2
player_2_vel = 2
dot_x,dot_y = rt(0,1000),rt(0,600)
name_1 = "Neil"
name_2 = "Al Goh"
game_over = False
fullscreen = False
player_1 = Player(name_1,50,50,(0,0,255),10,player_vel,1)
player_2 = Player(name_2,950,550,(255,0,0),10,player_2_vel,2)





clock = pygame.time.Clock()

        
 


font = pygame.font.Font('freesansbold.ttf',20)
big_font = pygame.font.Font('freesansbold.ttf',64)

winner = " "

running = True
player_2.collide = False
player_1.collide = False
run_menu()
winner_declared = False
mixer.music.stop()
mixer.music.load('Game_on_music.mp3')
mixer.music.play(-1,0.0)

# Main loop

while running:
    
    mouse_x,mouse_y = pygame.mouse.get_pos()
    dot_x,dot_y = rt(0,1000),rt(0,600)
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        
    


        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((pygame.display.Info().w,pygame.display.Info().h),pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((pygame.display.Info().w,pygame.display.Info().h),pygame.FULLSCREEN)

    
    for j in range(1000):
        if player_1.direction == "UP":
            dot_y_list[j] += player_1.vel
        if player_1.direction == "DOWN":
            dot_y_list[j] -=player_1.vel
       
        if check_collision(player_1.radius,dot_x_list[j],dot_y_list[j],player_1.x,player_1.y):
            dot_x_list[j] = rt(0,1000)
            dot_y_list[j] = rt(0,600)
            player_1.radius+=0.1
            
        if check_collision(player_2.radius,dot_x_list[j],dot_y_list[j],player_2.x,player_2.y):
            dot_x_list[j] = rt(0,1000)
            dot_y_list[j] = rt(0,600)
            player_2.radius+=0.1          

        if winner_declared is True:
            dot_y_list[j]+=dot_vel_list[j]
            game_over = True

        pygame.draw.circle(screen,dot_color_list[j],(dot_x_list[j],dot_y_list[j]),dot_radius_list[j])

    if check_collision(player_1.radius,player_1.x,player_1.y,player_2.x,player_2.y):
        if player_1.radius>player_2.radius:
            player_2.collide = True
            winner_declared = True
            player_1.vel = 0
            player_1.x = 1000/2-player_1.radius
            player_1.y = 600/2-player_1.radius + 70
            winner = player_1.name
            
    if check_collision(player_1.radius,player_1.x,player_1.y,player_2.x,player_2.y):
        if player_1.radius<player_2.radius:
            player_1.collide = True


    if check_collision(player_1.radius,player_1.x,player_1.y,player_2.x,player_2.y):
        if player_1.radius<player_2.radius:
            player_1.collide = True
            winner_declared = True
            player_2.vel = 0
            player_2.x = 1000/2-player_1.radius
            player_2.y = 600/2-player_1.radius + 70
            winner = player_2.name
            
    if check_collision(player_1.radius,player_1.x,player_1.y,player_2.x,player_2.y):
        if player_2.radius>player_1.radius:
            player_2.collide = True
    if game_over is True:
        show_winner(winner)
  
    player_2.draw(screen)
    player_1.draw(screen)  
     
    show_text()

    if game_over is True:
        show_winner(winner)


    pygame.display.update()
    clock.tick(60)


    

    print(player_2.direction)

