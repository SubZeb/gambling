from itertools import product
from random import randint


def roll(number_of_dice, number_of_sides=6):
    throw = []
    for i in range(number_of_dice):
        throw.append(randint(1, number_of_sides))
    return throw


def probability(number_of_dice, target=None, sides=6):
    dice = list(product(list(i for i in range(1, sides+1)), repeat=number_of_dice))
    totals = {}
    for i in dice:
        if not sum(i) in totals:
            totals[sum(i)] = 1
        else:
            totals[sum(i)] += 1
    sort_totals = sum(v for v in totals.values())
    prob = {}
    for k, v in totals.items():
        prob[k] = v / sort_totals
    for k, v in prob.items():
        prob[k] = round(float(v) * 100, 3)
    if target:
        answer = prob[str(target)]
    else:
        answer = prob
    return answer


