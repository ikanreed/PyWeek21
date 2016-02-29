from areas.area import Area
from objects.interactable import Interactable

class Hall(Area):
    def __init__(self, game):
        super(Hall, self).__init__(game)
        self.background=game.backgroundimage('hallway')
        self.name="Hall ad nauseum"
        self.objects=[
            Interactable(game, self.gotoGym, 'Enter the gym',
                "You'd think a hallway would be a good way to get to the next class.",0, 200)]
    def gotoGym(self, item):
        if not item:
            self.game.changeArea('Gym')
        pass
