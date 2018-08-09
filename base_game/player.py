from resources.missions import Mission

class Player():
    """ Player base class """

    def __init__(self, player_name: str, armies: dict, color, mission: Mission):
        # some safety checks
        avail_colors = 'BLUE RED GREEN BLACK YELLOW PURPLE'.split()
        if color not in avail_colors:
            raise ValueError(f'color {color} Not valid, expecte: {avail_colors}')
       
       
        self.player_name = player_name
        self.color = color
        self.armies = armies
        self.mission = mission
        self.winner = False
        self.alive = True
        self.eliminated_players = []
        
    def ressuply_troops(self, troops: dict):
        """
        Given the number of occupied territories, continets,
        add troops to selected territories. 
        """
        pass
    
    def attack(self, origin: str, target: str, n_troops: int):
        """
        Attacks an adjacent territory from another player
        """
        pass
    
    def fortify(self, origin: str, target: str, n_troops: int):
        """
        Move trops from one territory to a connected territory
        """
        pass
    
    def pickup_card(self):
        """
        Pick up a territory card after winning turn
        """
        pass

    def wins(self):
        self.winner = True
    