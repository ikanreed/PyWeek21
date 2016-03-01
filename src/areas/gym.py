from areas.area import Area
from objects.interactable import Interactable

class Gym(Area):
    def __init__(self, game):
        super(Gym, self).__init__(game)
        self.background=game.backgroundimage('gym')
        self.name="Gym ad nauseum"
        self.showprotagonist=True
        self.objects=[
            Interactable(game, self.gotohall, 'Exit to hallway',
                "You'd think a hallway would be a good way to get to the next class.",0, 200)]
    def gotohall(self, item):
        if not item:
            self.game.changeArea('Hall',(500,275))
        pass
