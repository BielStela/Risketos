class Player():
    """ Player base class """

    def __init__(self, player_name: str, armies: dict, objective):
        raise NotImplementedError
        self.player_name = player_name
        self.armies = armies
        
        self.objective = 

    def ressuply_troops(self):
        pass
    
    def attack(self):
        pass
    
    def fortify(self):
        pass
    
    def pickup_card(self):
        pass
    