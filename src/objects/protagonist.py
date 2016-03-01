class Protagonist:
    def __init__(self, game):
        self.game=game
        self.idlesprite=game.sprite('protagonist')
        self.currentimage=self.idlesprite[0]
        self.frames=0
        self.endaction=None
        self.enditem=None
        self.pos=(0,0)
        self.target=None
    def update(self):
        if self.target:
            tx,ty=self.target
            tx=tx-self.currentimage.get_rect().width//2
            ty=ty-self.currentimage.get_rect().height//2
            px,py=self.pos
            if (tx-px)**2+(ty-py)**2<9:
                self.pos=(tx,ty)
                self.target=None
                self.currentimage=self.idlesprite[0]
                self.frames=0
                if self.endaction:
                    self.endaction(self.enditem)
                    self.endaction=None
                    self.enditem=None
            else:
                if self.pos[0]<tx:
                    self.pos=self.pos[0]+3,self.pos[1]
                if self.pos[0]>tx:
                    self.pos=self.pos[0]-3,self.pos[1]
                if self.pos[1]<ty:
                    self.pos=self.pos[0],self.pos[1]+3
                if self.pos[1]>ty:
                    self.pos=self.pos[0],self.pos[1]-3
                
        else:
            self.currentimage=self.idlesprite[self.frames%len(self.idlesprite)]
        self.frames+=1
    def draw(self):
        x,y=self.pos
        startx,starty=self.game.gamearea.topleft
        self.game.window.blit(self.currentimage,(x+startx,y+starty))