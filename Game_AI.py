import pygame
from random import randint as rt
from Functions import *
import sys
pygame.init()


class Enemy:
    def __init__(self,level,name,x,y,color,radius,vel,Dot_pos_X,Dot_pos_Y):
        self.level = level
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.vel = vel
        self.collide = False
       
        self.name = name
        self.safe = True
        self.Dot_pos_X = Dot_pos_X
        self.Dot_pos_Y = Dot_pos_Y

        self.num_of_dots_N_list = []
        self.num_of_dots_E_list = []
        self.num_of_dots_S_list = []
        self.num_of_dots_W_list = []

        self.total_dot_list = []
        self.max_dot = int()
        self.direction = " "



        
        self.update()
    
    def draw(self,win):
      
        self.move()

        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
    
    def move(self):
        self.count_dots()
        if self.direction == "N" :
            self.y-=self.vel
        if self.direction == "S":
            self.y+=self.vel
        if self.direction == "E":
            self.x+=self.vel
        if self.direction == "W":
            self.x-=self.vel

 
        self.check_borders()
        self.update() 
    
    def check_borders(self):
        if self.collide == False:
            if self.x<=0+self.radius:
                self.x =0+self.radius
            if self.x>=1000-self.radius:
                self.x = 1000-self.radius
            if self.y<=0+self.radius:
                self.y = 0+self.radius
            if self.y>=600-self.radius:
                self.y = 600-self.radius
        else:
            self.y = -2000
            self.vel = 0


    def check_dots_north(self):
        
       
        for i in range(1000): 
            if self.Dot_pos_X[i] in range(self.x-int(self.radius),self.x+int(self.radius)):
                if self.Dot_pos_Y[i] in range(int(self.y-200),int(self.y)):
               
                    self.num_of_dots_N_list.append((self.Dot_pos_X[i],self.Dot_pos_Y[i]))
        self.check_borders()        
        
        return self.num_of_dots_N_list


    def check_dots_east(self):
     
        for i in range(1000): 
            if self.Dot_pos_Y[i] in range(int(self.y-int(self.radius)),int(self.y+int(self.radius))):
                if self.Dot_pos_X[i] in range(int(self.x),int(self.x+200)):
               
                    self.num_of_dots_E_list.append((self.Dot_pos_X[i],self.Dot_pos_Y[i]))
                
        self.check_borders()



    def check_dots_south(self):
        
        for i in range(1000): 
            if self.Dot_pos_X[i] in range(self.x-int(self.radius),self.x+int(self.radius)):
                if self.Dot_pos_Y[i] in range(int(self.y),int(self.y+200)):
               
                    self.num_of_dots_S_list.append((self.Dot_pos_X[i],self.Dot_pos_Y[i]))
                
        self.check_borders()



    def check_dots_west(self):
      
        for i in range(1000): 
            if self.Dot_pos_Y[i] in range(self.y-int(self.radius),self.y+int(self.radius)):
                if self.Dot_pos_X[i] in range(int(self.x-200),int(self.x)):
               
                    self.num_of_dots_W_list.append((self.Dot_pos_X[i],self.Dot_pos_Y[i]))
                
        self.check_borders()

    

    def count_dots(self):
    
        self.update()
        self.check_dots_north()
        self.check_dots_east()
        self.check_dots_south()
        self.check_dots_west()



        self.total_dot_list.append(len(self.num_of_dots_N_list))
        self.total_dot_list.append(len(self.num_of_dots_E_list))
        self.total_dot_list.append(len(self.num_of_dots_S_list))
        self.total_dot_list.append(len(self.num_of_dots_W_list))

        self.max_dot = max(self.total_dot_list)

   
        if self.total_dot_list[0] == self.max_dot:
            self.direction == "N"
        elif self.total_dot_list[1] == self.max_dot:
            self.direction == "E"
        elif self.total_dot_list[2] == self.max_dot:
            self.direction == "S"
        elif self.total_dot_list[3] == self.max_dot:
            self.direction == "W"

        

        



    def __del__(self):
        print("object delete")

    def update(self):
        self.ellipse = ((self.x,self.y),self.radius)

      












