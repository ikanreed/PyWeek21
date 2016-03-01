from areas.area import Area
from objects.interactable import Interactable

class Hall(Area):
    def __init__(self, game):
        super(Hall, self).__init__(game)
        self.background=game.backgroundimage('hallway')
        self.name="Hollow Hallway"
        self.showprotagonist=True
        self.objects=[
            Interactable(game, self.gotoGym, 'Enter the gym',
                "I've lost a lot of weight at the school gymnasium.  I think they're still looking for the 3 pound dumbell",500, 250)]
    def gotoGym(self, item):
        if not item:
            self.game.changeArea('Gym',(50,300))
        pass
