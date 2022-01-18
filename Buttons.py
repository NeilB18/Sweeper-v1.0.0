from types import FunctionType
import pygame


pygame.init()

class Button:
   
    def __init__(self,x,y,width,height):
        self.x = x
        self.y =y 
        self.width = width
        self.height = height
        self.mouse_click = False
        self.update()
    def check_if_clicked(self):
        if self.mouse_click == True:
            return True
        else:
            return False
    def make_short_cut(self,function,x1,y1,highlighted_pic,screen,x2,y2):

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_click = True

        if self.Rect.collidepoint((x1,y1)):
            screen.blit(highlighted_pic,(x2,y2))
            if self.check_if_clicked():
                function
            else:
                print("Error ... :(")
        self.update()
    def update(self):
        self.Rect = pygame.Rect(self.x,self.y,self.width,self.height)


