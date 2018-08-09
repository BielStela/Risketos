from itertools import combinations
from collections import defaultdict
from collections import Counter
from typing import List, Dict 

import yaml

class Board():
    """
    Base map class.

    Each player has an instance of the map with the number 
    of units in each country.
    """
    REGIONS_FILE = './resources/regions.yaml' 

    def __init__(self, players: List[str]):
        
        self.regions = self.read_regions_file(self.REGIONS_FILE)

        self.players_map = self.__init_players(players)
        # if not armies:
        #     self.armies_map = self.base_map
        # else:
        #   self.armies_map = dict(Counter(self.base_map).update(armies))

        # self.continent_connections = {('EUROPE', 'ASIA'),
        #                     ('EUROPE', 'AFRICA'),
        #                     ('AFRICA', 'SOUTH AMERICA'),
        #                     ('SOUTH AMERICA', 'NORTH AMERICA'),
        #                     ('NORTH AMERICA', 'EUROPE'),
        #                     ('NORTH AMERICA', 'ASIA'),
        #                     ('ASIA', 'OCEANIA'),}

    

    def __repr__(self):
        return str(self.regions)
    
    def update_map(self, armies):
        pass
    
    
    def __init_players(self, players: List[str]):
        pass
    
    def __read_regions_file(self, file: str) -> dict:
        with open(file) as f:
            regions: dict = yaml.load(f)
        
        return regions