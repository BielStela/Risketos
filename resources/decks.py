from collections import namedtuple
import random
from typing import List, Dict 

from base_game.map import Board 

class TerritoryDeck():

    def __init__(self):

        self.card = namedtuple('Card', ['value', 'country', 'wildcard'])
        self.cards = self._init_cards()
    
    def _init_cards(self) -> list:
        """ returns a shufled deck of territory cards"""
        VALUES = [1, 2, 3, 4]  # 4 stands for wildcard 
        countries =  Board([]).countries
        #infantry
        countries_1 = ['Venezuela',
                       'Siam',
                       'Peru',
                       'New Guinea',
                       'Mongolia',
                       'Middle East',
                       'Kamchatka',
                       'Iceland', 
                       'Egypt',
                       'East Africa',
                       'China',
                       'Central Africa',
                       'Argentina',
                       'Alaska']
        # horses
        countries_2 = ['Afghanistan',
                       'Alberta',
                       'Quebec',
                       'Greenland', 
                       'India',
                       'Irkutsk',
                       'Madagascar',
                       'North Africa',
                       'Ontario',
                       'Ukraine',
                       'Scandinavia',
                       'Siberia',
                       'Ural',
                       'Yakutsk']
        # cannons
        countries_3 = list(set(countries) - set(countries_1) - set(countries_2))

        cards = [self.card(1, country, False) for country in countries_1]
        cards.extend([self.card(2, country, False) for country in countries_2])
        cards.extend([self.card(3, country, False) for country in countries_3])
        cards.extend([self.card(4,'', True)]*2)
        
        random.shuffle(cards)
        return cards

