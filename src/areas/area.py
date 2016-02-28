class Area:
    def __init__(self, game):
        self.game=game
        self.background=None
        self.objects=[]
        self.activeobject=None
        self.name="Nowhere in particular"
    def click(self):
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
    def mousemove(self,x,y):
        y=y-94
        for object in self.objects:
            if object.rect.collidepoint(x,y):
                self.activeobject=object
                return
        self.activeobject=None