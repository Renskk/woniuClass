from random import randint


def attack_damage(mod):
    roll = randint(1, 8)
    return mod + roll
