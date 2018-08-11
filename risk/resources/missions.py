from typing import List

# from risk.base_game.player import Player

"""
Dict of mission functions. Every mission is a function assignet to a player.

When called it checks the winning rules and
assigns True to .winner property of the plaer
"""

# base mision funcs
def _eliminate_player_mission(player, target_color: str):
    """
    Check if player eliminated target color
    """

    # if not isinstance(player, Player):
    #     raise ValueError(f"{player} must be `Player` class")

    if player.color == target_color:
        # occupy 24 territories
        if len(player.territories) == 24:
            player.wins()
        else:
            pass
    
    elif target_color in player.eliminated_players:
        player.wins()

def _conquer_continent_mission(player, targets: List[str]):
    """
    Check if player occupied target continents 
    """

    # if not isinstance(player, Player):
    #     raise ValueError(f"{player} must be `Player` class")

    if all(target in player.continents for target in targets):
        player.wins()

#################
# Eliminate player Misions
#################

def mission1(player):
    """Destroy all BLUE troops. 
    if you are blue player, occupy 24 territories 
    """
    _eliminate_player_mission(player, 'BLUE')

def mission2(player):
    """Destroy all RED troops. 
    if you are red player, occupy 24 territories 
    """
    _eliminate_player_mission(player, 'RED')

def mission3(player):
    """Destroy all GREEN troops. 
    if you are green player, occupy 24 territories 
    """
    _eliminate_player_mission(player, 'GREEN')

def mission4(player):
    """Destroy all BLACK troops. 
    if you are black player, occupy 24 territories 
    """
    _eliminate_player_mission(player, 'BLACK')

def mission5(player):
    """Destroy all YELLOW troops. 
    if you are yellow player, occupy 24 territories 
    """
    _eliminate_player_mission(player, 'YELLOW')
    

def mission6(player):
    """Destroy all PURPLE troops. 
    if you are purple player, occupy 24 territories 
    """
    _eliminate_player_mission(player, 'PURPLE')

#################
# Conquer Misions
#################

def mission7(player):
    """Conquer the continents of ASIA and AFRICA."""
    conts = ['ASIA', 'AFRICA']
    _conquer_continent_mission(player, conts)

def mission8(player):
    """Conquer the continents of NORTH AMERICA and AUSTRALIA."""
    conts = ['NORTH AMERICA', 'AUSTRALIA']
    _conquer_continent_mission(player, conts)

def mission9(player):
    """Conquer the continents of NORTH AMERICA and AFRICA."""
    conts = ['NORTH AMERICA', 'AFRICA']
    _conquer_continent_mission(player, conts)

def mission10(player):
    """Conquer the continents of ASIA and SOUTH AMERICA."""
    conts = ['ASIA','SOUTH AMERICA']
    _conquer_continent_mission(player, conts)


_MISSIONS_DICT = {
    'mission1' : mission1,
    'mission2' : mission2,
    'mission3' : mission3,
    'mission4' : mission4,
    'mission5' : mission5,
    'mission6' : mission6,
    'mission7' : mission7,
    'mission8' : mission8,
    'mission9' : mission9,
    'mission10' : mission10,
    }