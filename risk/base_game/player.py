from risk.resources.decks import TerritoryDeck
from risk.resources.missions import _MISSIONS_DICT
from risk.base_game.utils import battle

class Player():
    """ Player base class """

    def __init__(self, player_name: str, territories: list, color: str, mission: str, board, init_armies: int):
        # some safety checks
        avail_colors = 'BLUE RED GREEN BLACK YELLOW PURPLE'.split()
        if color not in avail_colors:
            raise ValueError(f'color {color} not valid, expected: {avail_colors}')
       
        self.board = board
        self.player_name = player_name
        self.color = color

        self.territories = territories
        self.init_armies = init_armies
        
        self._mission = _MISSIONS_DICT[mission] 
        self.winner = False
        self.alive = True
        self.territ_cards = []
        self.eliminated_players = []
        self.n_troops = 0

    def __str__(self):
        s = (f'Name: {self.player_name}\n'
             f'Color: {self.color}\n'
             f'Mission: {self.show_mission()}\n')
        return s
    
    def __repr__(self):
        s = f'Player({self.player_name}, {self.color})'
        return s
        
    def get_reinforcement_troops(self):
        """
        Given the number of occupied territories and continets,
        get troops for ressuply. 
        """
        extra_troops_terr = len(self.territories) // 3

        continent_owned = []
        for cont, terr in self.board.regions.items():
            if set(terr) == set(self.territories):
                continent_owned.append(cont)
        
        continent_troops = {
            'ASIA':7,
            'NORTH AMERICA':5,
            'EUROPE':5,
            'AFRICA':3,
            'AUSTRALIA':2,
            'SOUTH AMERICA':2
        }

        extra_troops_cont = sum([continent_troops[cont] for cont in continent_owned])

        reinforcements = extra_troops_cont + extra_troops_terr
        return reinforcements
    
    
    
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
    