from random import sample
from itertools import combinations
from collections import defaultdict
from collections import Counter
from typing import List, Dict 

from risk.base_game.map import Board
from risk.base_game.player import Player
from risk.resources.decks import TerritoryDeck
from risk.resources.missions import _MISSIONS_DICT

class Risk():
    '''
    Risk base class. 
    '''

    def __init__(self, n_players: int) -> None:
        
        self.players = self.init_players(n_players)
        self.board = Board(self.players)
        self.region_map = self.board.regions
    
    def __repr__(self):
        return 'Risk Game'
    
    def _update_global_map(self, armies: dict) -> None:
        """
        Updates global map with new units
        """
        new_map = dict(Counter(self.global_map).update(armies))
        self.global_map.update(new_map)

    def init_players(self, n_players):
        """
        Creates n players with a random mission, random army distribution
        according to board rules (No need to use terrytory deck)
        """

        all_missions = _MISSIONS_DICT.keys()
        # pickup random subset of missions
        misisons = sample(all_missions, n_players)  

        avail_colors = 'BLUE RED GREEN BLACK YELLOW PURPLE'.split()
        colors = sample(avail_colors, n_players)

        players = []
        for i, (mission, color) in enumerate(zip(misisons, colors)):
            p_name = f'player_{i}'
            p = Player(p_name, {}, color, mission)
            players.append(p)
        
        return players
    
    def add_player(self, player: str, armies: dict) -> None:
        """
        Adds player and updates player map
        """
        # first player
        if not self.players:
            self.players.append(player)
            self.players_map[player] = Board(armies=armies)
            self._update_global_map(armies)

        # check if player exists
        elif player in self.players:
            raise ValueError(f'player {player} already exists')

        # new player in instance with others players
        else:
            # check is armies are in occupied countries
            occupied_countries = []
            for country, units in self.global_map.items():
                if units > 0:
                    occupied_countries.append(country)

            for country, units in armies.items():
                if units > 0:
                    if country in occupied_countries:                    
                        raise ValueError(f'Country {country} already occupied by other player')
            
            self.players.append(player)
            self.players_map[player] = Map(armies)
            self._update_global_map(armies)

    def get_neightbours(self, country: str) -> list:
        neightbours = []
        for s in self.world.connections:
            if country in s:
                for c in s:
                    if c != country:
                        neightbours.append(c)
        return neightbours
    
    
