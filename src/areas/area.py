class Area:
    def __init__(self, game):
        self.game=game
        self.background=None
        self.objects=[]
        self.activeobject=None
        self.showprotagonist=False
        self.name="Nowhere in particular"
    def click(self):
        if self.activeobject :
            if self.showprotagonist:
                #have the protagonist walk to the target THEN use it
                self.game.protagonist.target=self.activeobject.rect.center
                self.game.protagonist.endaction=self.activeobject.action
                self.game.protagonist.enditem=self.game.item
            else:
                self.activeobject.action(self.game.item)
        elif self.showprotagonist:
            x,y=self.game.lastpos
            self.game.protagonist.target=(x-self.game.gamearea.left,y-self.game.gamearea.top)
        pass
    def right_click(self):
        pass

    def draw(self):
        if self.background:
            self.game.window.blit(self.background,(0,94))
        for object in self.objects:
            rect=object.rect.copy()
            rect.top+=94
            self.game.window.blit(object.animation[self.game.frame%len(object.animation)], rect)
        if self.showprotagonist:
            self.game.protagonist.draw()
    def mousemove(self,x,y):
        y=y-94
        for object in self.objects:
            if object.rect.collidepoint(x,y):
                self.activeobject=object
                return
        self.activeobject=None
