from random import choice

def battle(attackers: int, defenders: int, n_attack_dices: int, n_defend_dices: int):
    if n_attack_dices > 3 or n_attack_dices <= 0:
        raise ValueError('invalid number of attack dices. Must be between [1,3]')
    
    if n_defend_dices > 2 or n_defend_dices <= 0:
        raise ValueError('invalid number of defender dices. Must be 1 or 2')
    
    DICE = range(1,7)
    
    attack_throw = [choice(DICE) for _ in range(n_attack_dices)]
    defence_throw = [choice(DICE) for _ in range(n_defend_dices)]

    attack_largest = _n_largest(attack_throw, n_defend_dices)

    res = [a > b for a, b in zip(attack_largest, defence_throw)]

    # defender loses
    defenders -= sum(res)
    # attacker loses
    attackers -= sum([1-val for val in res])

    return attackers, defenders

def _n_largest(iterable, n):
    if len(iterable) == 1:
        return max(iterable)
    return sorted(iterable, reverse=True)[:n]