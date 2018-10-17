from itertools import combinations
from collections import defaultdict
from collections import Counter
from typing import List, Dict
from pathlib import Path
import os
from collections import namedtuple

import pandas as pd
import yaml

# from risk.base_game import Player


class Board:
    """
    Base map class.

    Each player has an instance of the map with the number 
    of units in each country.
    """

    def __init__(self):
        # dict with {continent:[territories]}
        self.continents = self.read_continents_file()
        # [territories]
        self.territories = [item for sublist in self.continents.values()
                            for item in sublist]

        self.player_board = self.init_player_board()

        self.adjacency_mat = self.read_adjacency_matrix()
        # self.players_map = self.__init_players(players)
        # if not armies:
        #     self.armies_map = self.base_map
        # else:
        #   self.armies_map = dict(Counter(self.base_map).update(armies))

    def __repr__(self):
        return str(self.player_board)

    def update_map(self, armies):
        pass

    @staticmethod
    def read_continents_file() -> dict:
        """
        Reads the continents yaml and returns a dict with
        {Continent: [Territories]}
        """
        this_dir = Path(__file__).parent.parent
        continents_path = os.path.join(
            str(this_dir), "resources", "data", "continents.yaml")

        with open(continents_path) as f:
            continents = yaml.load(f)

        return continents

    @staticmethod
    def read_adjacency_matrix() -> pd.DataFrame:
        """
        Reads the adjacency matrix and returns a DataFrame
        """
        this_dir = Path(__file__).parent.parent
        ADJ_MAT_PATH = os.path.join(
            str(this_dir), "resources", "data", "adjacency_matrix.csv")

        df = pd.read_csv(ADJ_MAT_PATH, index_col=0)
        return df

    def get_neightbours(self, territory: str) -> list:
        """
        Returns list of neightbour territories to given territory
        via adjacency matrix
        """

        territory_series = self.adjacency_mat.loc[territory]
        neightbours = territory_series[territory_series == 1]
        return list(neightbours.index)

    def init_player_board(self) -> dict:
        """
        Creates dict with territories, player
        and armies to keep track of the status of the game
        """
        # territory = namedtuple('Territory', ['name', 'player', 'troops'])

        # territories_dict = {cont: [territory(name, '', 0) for name in terrs]
        #                     for cont, terrs in self.continents.items()}

        territories_dict = {name: {'player': '', 'troops': 0}
                            for name in self.territories}
        return territories_dict
