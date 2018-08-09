
from itertools import combinations
from collections import defaultdict
from collections import Counter
from typing import List, Dict 

from base_game.map import Board

class Risk():
    '''
    Risk base class. 
    '''

    def __init__(self, players: List[str]) -> None:
        
        self.board = Board()
        self.region_map = self.board.regions
        self.players_map = {}
        self.players = players
    
    def __repr__(self):
        return str(self.players_map)
    
    def _update_global_map(self, armies: dict) -> None:
        """Updates global map with new units"""
        new_map = dict(Counter(self.global_map).update(armies))
        self.global_map.update(new_map)

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
    
    
