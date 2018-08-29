from itertools import combinations
from collections import defaultdict
from collections import Counter
from typing import List, Dict 
from pathlib import Path
import os

import pandas as pd

import yaml

from risk.base_game import Player

class Board():
    """
    Base map class.

    Each player has an instance of the map with the number 
    of units in each country.
    """
  
    def __init__(self):
        
        self.regions = self.read_regions_file()
        self.territories = [item for sublist in self.regions.values() for item in sublist]

        self.adjacency_mat = self.read_adjacency_matrix()
        #self.players_map = self.__init_players(players)
        # if not armies:
        #     self.armies_map = self.base_map
        # else:
        #   self.armies_map = dict(Counter(self.base_map).update(armies))    

    def __repr__(self):
        return str(self.regions)
    
    def update_map(self, armies):
        pass
    
    def read_regions_file(self) -> dict:
        """
        Reads the regions yaml and returns a dict with
        {Continent: [Territories]}
        """
        this_dir = Path(__file__).parent.parent
        REGIONS_PATH = os.path.join(str(this_dir), "resources", "data", "regions.yaml")

        with open(REGIONS_PATH) as f:
            regions: dict = yaml.load(f)
        
        return regions
    
    def read_adjacency_matrix(self) -> pd.DataFrame:
        """
        Reads the adjacency matrix and returns a DataFrame
        """
        this_dir = Path(__file__).parent.parent
        ADJ_MAT_PATH = os.path.join(str(this_dir), "resources", "data", "adjacency_matrix.csv")

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
    
    def init_players(self):
        """
        Update the record of what players owns every territory
        """
        pass
        
