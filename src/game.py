import pygame, sys
from pygame.locals import *

pygame.init()

class Game:
    def __init__(self):
        self.window=pygame.display.set_mode((992, 736))
        self.mainbackground=self.backgroundimage('fullscreen')
        self.clock=pygame.time.Clock()
        self.window.set_colorkey((20,60,80))
    def run(self):
        while True:
            self.window.blit(self.mainbackground,(0,0))
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(30)
        
        
    def backgroundimage(self, name):
        return pygame.image.load('../graphics/backgrounds/%s.png'%name)

        
        
if __name__=="__main__":
	game=Game()
	game.run()