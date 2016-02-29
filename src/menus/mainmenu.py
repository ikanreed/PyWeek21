import pygame, sys
from pygame.locals import *
from areas import *


class MainMenu:
    def __init__(self,game):
        self.game=game
        self.focuscolor=(128,0,0)
        self.unfocuscolor=(0,0,0)
        self.highlightindex=None
        if game.area:
            self.options=[("Resume", self.resume),("New", self.new),("Credits", self.credits),("Quit", self.quit)]
        else:
            self.options=[("New", self.new),("Credits", self.credits),("Quit", self.quit)]
        self.rects=[]
        starty=94+20
        startx=200
        for i in range(len(self.options)):
            name, effect=self.options[i]
            blob=self.game.font.render(name, True, self.unfocuscolor, None)
            rect=blob.get_rect()
            rect.topleft=(startx, starty+i*36)
            self.rects.append(rect)
    def draw(self):
        for i in range(len(self.options)):
            color=self.unfocuscolor
            if self.highlightindex is not None and i==self.highlightindex:
                color=self.focuscolor
            name, effect=self.options[i]
            blob=self.game.font.render(name, True, color, None)
            self.game.window.blit(blob, self.rects[i])
    def click(self):
        if self.highlightindex is not None:
            self.options[self.highlightindex][1]()
    def mousemove(self, x, y):
        index=0
        for rect in self.rects:
            if rect.left<=x and rect.right >= x and rect.top<=y and rect.bottom >= y:
                self.highlightindex=index
                return
            index+=1
        self.highlightindex=None
    def new(self):
        self.game.areas={'Gym':gym.Gym(self.game), 'Hall':hall.Hall(self.game)}
        self.game.inventory=[]
        self.game.area=self.game.areas['Gym']
        self.game.menu=None
    def resume(self):
        self.game.menu=None
    def credits(self):
        pass
    def quit(self):
        pygame.quit()
        sys.exit()
