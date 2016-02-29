import pygame, sys
from pygame.locals import *
from areas.gym import Gym
from areas.hall import Hall
from menus.mainmenu import MainMenu

pygame.init()

class Game:
    def __init__(self):
        self.gamearea=pygame.Rect(0,94,783,642)
        self.inventoryarea=pygame.Rect(783,94,209,642)
        self.window=pygame.display.set_mode((992, 736))
        self.mainbackground=self.backgroundimage('fullscreen')
        self.clock=pygame.time.Clock()
        self.font=pygame.font.Font('../ballpointprint.ttf',16*2)
        self.window.set_colorkey((20,60,80))
        self.area=None
        self.menu=MainMenu(self)
        self.item=None
        self.inventory=[]
        self.completedflags=[]
        self.areas={}
        self.activecutscene=None
        self.ticks=0
        self.frames=0

    def run(self):
        while True:
            self.window.blit(self.mainbackground,(0,0))
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if self.activecutscene:
                    continue
                if event.type==MOUSEMOTION:
                    pos=event.pos
                    self.lastpos=pos
                    if self.menu:
                        self.menu.mousemove(pos[0],pos[1])
                    elif self.area:
                        self.area.mousemove(pos[0],pos[1])
                elif event.type==MOUSEBUTTONUP:
                    if event.button==1:
                        if self.menu:
                            self.menu.click()
                        elif self.area:
                            if self.lastpos:
                                if self.gamearea.collidepoint(self.lastpos):
                                    self.area.click()
                                elif self.inventoryarea.collidepoint(self.lastpos):
                                    self.pickItem(self.lastpos)
                            self.item=None
                    if event.button==2:
                        if self.area and not self.menu:
                            if self.lastpos:
                                if self.gamearea.collidepoint(self.lastpos):
                                    self.area.right_click()
                                if self.inventoryarea.collidepoint(self.lastpos):
                                    self.describeItem(self.lastpos)
            if self.area and self.area.name:
                blob=self.font.render(self.area.name,True, (0,0,0), None)
                rect=blob.get_rect()
                rect.topleft=(180, 25)
                self.window.blit(blob, rect)
            if self.area and self.area.activeobject and self.area.activeobject.name:
                blob=self.font.render(self.area.activeobject.name,True, (0,0,0), None)
                rect=blob.get_rect()
                rect.topleft=(455, 25)
                self.window.blit(blob, rect)
            if self.menu:
                self.menu.draw()
            elif self.area:
                self.area.draw()
            self.ticks+=1
            self.frame=self.ticks//3
            pygame.display.update()
            self.clock.tick(30)


    def backgroundimage(self, name):
        return pygame.image.load('../graphics/backgrounds/%s.png'%name)
    def sprite(self, name, frames=0):
        if frames:
            return [pygame.image.load('../graphics/sprites/%s-%i.png'%(name, frame)) for frame in range(frames)]
        else:
            return [pygame.image.load('../graphics/sprites/%s.png'%name)]
    def pickItem(self, pos):
        pass
    def describeItem(self,pos):
        pass

    def changeArea(self,new):
        self.area=self.areas[new]

        pass

if __name__=="__main__":
	game=Game()
	game.run()
