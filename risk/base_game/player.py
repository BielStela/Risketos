from risk.resources.decks import TerritoryDeck
from risk.resources.missions import _MISSIONS_DICT

class Player():
    """ Player base class """

    def __init__(self, player_name: str='', armies: dict={}, color='', mission: str=''):
        # some safety checks
        avail_colors = 'BLUE RED GREEN BLACK YELLOW PURPLE'.split()
        if color not in avail_colors:
            raise ValueError(f'color {color} not valid, expected: {avail_colors}')
       

        self.player_name = player_name
        self.color = color
        self.armies = armies
        self._mission = _MISSIONS_DICT[mission] # pass own instance of player
        self.winner = False
        self.alive = True
        self.territ_cards = []
        self.eliminated_players = []
    
    def __str__(self):
        s = (f'Name: {self.player_name}\n'
             f'Color: {self.color}\n'
             f'Mission: {self.show_mission()}\n')
        return s
    
    def __repr__(self):
        s = f'Player({self.player_name}, {self.color})'
        return s
        
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
    
    def pickup_card(self, deck: TerritoryDeck) -> None:
        """
        Pick up a territory card from current game `TerritoryDeck` instance
        after winning turn
        """
        self.territ_cards.append(deck.retrive_card())
    
    def check_mission(self):
        """
        Runs mission function and changes the status of winning
        """
        self._mission(self)
    
    def show_mission(self) -> str:
        return self._mission.__doc__

    def wins(self):
        self.winner = True
    