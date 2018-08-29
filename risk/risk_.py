from random import sample, choice, shuffle
from itertools import combinations
from collections import defaultdict
from collections import Counter
from typing import List, Dict 

from risk.base_game.board import Board
from risk.base_game.player import Player
from risk.resources.decks import TerritoryDeck
from risk.resources.missions import _MISSIONS_DICT

class Risk():
    '''
    Risk base class. it handles the instances of Board and Player.
    It is also responsible for keeping track of the turns.
    '''

    def __init__(self, n_players: int) -> None:
        
        # params
        self.n_players = n_players
        self._check_params()

        # instances
        self.board = Board()
        self.region_map = self.board.regions
        # make players and populate board
        self.players = self.init_players(n_players)
       

    def _check_params(self):
        """
        Check instance parameters
        """
        if self.n_players < 2:
            raise ValueError('Must play with 2 or more players')

        if self.n_players == 2:
            raise NotImplementedError('2 players game is not implemented yet')
        

    def __repr__(self):
        return f'Risk Game of {self.n_players} players'
    

    def _update_global_map(self, armies: dict) -> None:
        """
        Updates global map with new units
        """
        new_map = dict(Counter(self.global_map).update(armies))
        self.global_map.update(new_map)


    def init_players(self, n_players):
        """
        Creates n players with a random mission, random army distribution
        according to board rules (No need to use terrytory deck), and 
        intance of the board
        """

        all_missions = _MISSIONS_DICT.keys()
        # pickup random subset of missions
        missions = sample(all_missions, n_players)  

        avail_colors = 'BLUE RED GREEN BLACK YELLOW PURPLE'.split()
        colors = sample(avail_colors, n_players)
        
        ## distribute random territories for each player
        # shuffled territories
        territories = self.board.territories
        shuffle(territories)
        # split the shuffled terrs in chunks for each player
        chunk_size = len(territories) // n_players
        chunks = [territories[i:i+chunk_size] for i in range(0, len(territories), chunk_size)]
        
        # number of initial troops given the number of players 
        init_armies_x_player = {3:35,4:30,5:25,6:20}
        player_armies = init_armies_x_player[n_players]
        

        players = []
        for i in range(n_players):
            p_name = f'player_{i}'

            p = Player(player_name=p_name,
                       territories=chunks[i],
                       color=colors[i],
                       mission=missions[i],
                       board=self.board,
                       init_armies=player_armies)

            players.append(p)
        
        return players
    





    # -----------------------------------------------------
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

    
    
    
