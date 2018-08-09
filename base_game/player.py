class Player():
    """ Player base class """

    def __init__(self, player_name: str, armies: dict, objective):
        raise NotImplementedError

        self.player_name = player_name
        self.armies = armies
        
        self.objective = None

        self.cards = []

    def ressuply_troops(self, troops: dict):
        pass
    
    def attack(self, origin: str, target: str, n_troops: int):
        pass
    
    def fortify(self, origin: str, target: str, n_troops: int):
        pass
    
    def pickup_card(self):
        pass
    