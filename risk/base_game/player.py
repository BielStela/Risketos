from risk.resources.decks import TerritoryDeck
from risk.resources.missions import MISSIONS_DICT

class Player():
    """ Player base class """

    def __init__(self, player_name: str='', armies: dict={}, color='', mission: str=''):
        # some safety checks
        avail_colors = 'BLUE RED GREEN BLACK YELLOW PURPLE'.split()
        if color not in avail_colors:
            raise ValueError(f'color {color} Not valid, expecte: {avail_colors}')
       

        self.player_name = player_name
        self.color = color
        self.armies = armies
        self.mission = MISSIONS_DICT[mission] # pass own instance of player
        self.winner = False
        self.alive = True
        self.territ_cards = []
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
    
    def pickup_card(self, deck: TerritoryDeck):
        """
        Pick up a territory card from current game `TerritoryDeck` instance
        after winning turn
        """
        self.territ_cards.append(deck.retrive_card())
    
    def check_mission(self):
        """
        Runs mission function and changes the status of winning
        """
        self.mission(self)

    def wins(self):
        self.winner = True
    