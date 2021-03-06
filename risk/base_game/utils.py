from random import choice


def dice_battle(n_attack_dices: int=3, n_defend_dices: int=2):
    nad = n_attack_dices
    ndd = n_defend_dices

    if nad > 3 or nad <= 0:
        raise ValueError(
            'invalid number of attack dices. Must be between [1,3]')

    if ndd > 2 or ndd <= 0:
        raise ValueError('invalid number of defender dices. Must be 1 or 2')

    DICE = range(1, 7)

    attack_throw = [choice(DICE) for _ in range(nad)]
    defence_throw = [choice(DICE) for _ in range(ndd)]

    attack_largest = _n_largest(attack_throw, ndd)

    battle_resu = [attk > deff for attk, deff in zip(attack_largest, defence_throw)]

    # defender loses
    defenders_lost = sum(battle_resu)
    # attacker loses. inerverse battle result
    attackers_lost = sum([1-val for val in battle_resu])

    return defenders_lost, attackers_lost


def _n_largest(iterable, n):
    return sorted(iterable, reverse=True)[:n]
