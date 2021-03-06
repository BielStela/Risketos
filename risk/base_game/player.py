from risk.resources.decks import TerritoryDeck
from risk.resources.missions import _MISSIONS_DICT
from risk.base_game.utils import dice_battle


class Player():
    """ Player base class """

    def __init__(self, name: str, territories: list,
                 color: str, mission: str, board, init_troops: int):

        # some safety checks
        avail_colors = 'BLUE RED GREEN BLACK YELLOW PURPLE'.split()
        if color not in avail_colors:
            raise ValueError(
                f'color {color} not valid, expected: {avail_colors}')

        self.__board = board  # game instance of board

        self.name = name
        self.color = color

        self.territories = territories
        self.continets = []  # TODO
        self._distribution = {}  # territory: troops

        self.init_troops = init_troops
        
        self.troops_to_distribute = init_troops  # counter

        self._mission = _MISSIONS_DICT[mission]
        self.winner = False
        self.alive = True
        self.territ_cards = []
        self.eliminated_players = []
        self.n_troops = 0  # TOTAL of troops

    def __str__(self):
        s = (f'Name: {self.name}\n'
             f'Color: {self.color}\n'
             f'Mission: {self.show_mission()}\n')
        return s

    def __repr__(self):
        s = f'Player({self.name}, {self.color})'
        return s

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    @property
    def distribution(self):
        """Builds the troops distribution dictionary"""

        board = self.__board.player_board

        dist = dict()
        for terr, pdict in board.items():
            if pdict['player'].name == self.name:
                dist[terr] = pdict['troops']

        self._distribution = dist
        return self._distribution

    @distribution.setter
    def distribution(self, new_distribution):
        """
        Updates distribution dict
        """
        self._distribution.update(new_distribution)

    def place_troops(self, phase: str, n: int) -> int:
        """Draws n units from reservoir.
        "init" from init_troops copy or "reinforce" for reinforcement phase
        """
        if phase == 'init':
            self.troops_to_distribute -= n
            return n

        if phase == 'reinforce':
            raise NotImplementedError

    def get_reinforcement_troops(self) -> int:
        """
        Given the number of occupied territories and continets,
        get troops for ressuply. 

        Uses the game instance of Board()
        """
        extra_troops_terr = len(self.territories) // 3

        continent_owned = []
        for cont, terr in self.__board.continents.items():
            if set(terr).issubset(self.territories):
                continent_owned.append(cont)

        continent_troops = {
            'ASIA': 7,
            'NORTH AMERICA': 5,
            'EUROPE': 5,
            'AFRICA': 3,
            'AUSTRALIA': 2,
            'SOUTH AMERICA': 2
        }

        extra_troops_cont = sum([continent_troops[cont]
                                 for cont in continent_owned])

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
