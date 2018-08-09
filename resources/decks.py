from collections import namedtuple
import random
from typing import List, Dict 

from base_game.map import Board 
from base_game.player import Player

class TerritoryDeck():

    def __init__(self):

        self.card = namedtuple('Card', ['value', 'country', 'wildcard'])
        self.cards = self._init_cards()
        self.disposed_cards = []

    def _init_cards(self) -> List[namedtuple]:
        """ returns a shufled deck of territory cards"""
        
        countries =  Board([]).countries
        #infantry
        countries_1 = ['Venezuela', 'Siam', 'Peru', 'New Guinea',
                       'Mongolia', 'Middle East', 'Kamchatka', 'Iceland', 
                       'Egypt', 'East Africa', 'China', 'Central Africa',
                       'Argentina', 'Alaska']
        # horses
        countries_2 = ['Afghanistan', 'Alberta', 'Quebec', 'Greenland',
                       'India', 'Irkutsk', 'Madagascar', 'North Africa',
                       'Ontario', 'Ukraine', 'Scandinavia', 'Siberia',
                       'Ural', 'Yakutsk']
        # canons
        countries_3 = list(set(countries) - set(countries_1) - set(countries_2))

        cards = [self.card(1, country, False) for country in countries_1]
        cards.extend([self.card(2, country, False) for country in countries_2])
        cards.extend([self.card(3, country, False) for country in countries_3])
        cards.extend([self.card(4,'', True)]*2)
        
        # SHUFFLE DECK
        random.shuffle(cards)
        return cards

    def retrive_card(self):
        card = self.cards.pop()
        return card
    
    def dispose_card(self, card):
        self.disposed_cards.append(card)




