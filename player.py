import random
import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((1000,600),pygame.RESIZABLE)

class Player:
    def __init__(self,name,x,y,color,radius,vel,player_number):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.ellipse = ((x,y),radius)
        self.player_number = player_number
        self.vel = vel
        self.collide = False
        self.fullscreen = False
        self.name = name
        self.ability = 0
        self.direction  =  ""
 
        self.update()



    
    def draw(self,win):
        self.move()
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
    



    def move(self):
        global running,dot_x,dot_y
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            running = False
            sys.exit()
        if self.player_number == 1:
            if keys[pygame.K_a]:
                self.x-=self.vel
                self.direction = "LEFT"
            if keys[pygame.K_d]:
                self.x+=self.vel
                self.direction = "RIGHT"
            if keys[pygame.K_w]:
                self.y-=self.vel
                self.direction = "UP"
            if keys[pygame.K_s]:
                self.y+=self.vel
                self.direction = "DOWN"
          
           
            self.check_borders()

        if self.player_number == 2:
            if keys[pygame.K_LEFT]:
                self.x-=self.vel
            if keys[pygame.K_RIGHT]:
                self.x+=self.vel
            if keys[pygame.K_UP]:
                self.y-=self.vel
            if keys[pygame.K_DOWN]:
                self.y+=self.vel 
            self.check_borders()
        
        self.update() 
    



    def check_borders(self):
        
        if self.collide == False:
            if self.x<=0+self.radius:
                self.x =0+self.radius
            if self.x>=screen.get_width()-self.radius:
                self.x = screen.get_width()-self.radius
            if self.y<=0+self.radius:
                self.y = 0+self.radius
            if self.y>=screen.get_height()-self.radius:
                self.y = screen.get_height()-self.radius
        else:
            self.y = -2000
            self.vel = 0




    def __del__(self):
        print("object delete")



    def update(self):
        self.ellipse = ((self.x,self.y),self.radius)
