import random

OREL = "OREL"
RESHKA = "RESHKA"
COIN_VALUES = [OREL, RESHKA]


def flip():
    return random.choice(COIN_VALUES)

print(flip())

def martingale(*, start_funds: int, min_bet: int, max_bet: int) -> int:
    steps_to_looose = 0
    current_funds = start_funds
    current_bet = min_bet

    while current_funds > 0:
        steps_to_looose += 1
        current_funds -= current_bet
        flipped_coin = flip()