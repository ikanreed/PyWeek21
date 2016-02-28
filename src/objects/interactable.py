class Interactable:
    def __init__(self, game,action, name, description, x=0, y=0, filename='invisible', frames=0,):
        self.game=game
        self.name=name
        self.frames=frames
        self.animation=game.sprite(filename, frames)
        self.rect=self.animation[0].get_rect()
        self.rect.topleft=(x,y)
        self.description=description
        self.action=action