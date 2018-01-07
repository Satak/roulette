"""Util functions."""

from random import choice
from typing import List
from models import Bet, Slot, Person
from bet_types import BET_TYPES
from controllers import (
    bet_type_1_ctrl,
    bet_type_2_ctrl,
    bet_type_3_ctrl
)

def init_bets() -> List[Bet]:
    """Bet initializer."""

    return [Bet(**bet) for bet in BET_TYPES]

def set_slot(num: int) -> Slot:
    """Set roulette Slot numbers and colors."""

    blacks: List[int] = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    color = 'RED'
    if num in blacks:
        color = 'BLACK'
    elif num == 0:
        color = 'WHITE'

    return Slot(number=num, color=color)

def spin_roulette(person: Person, amount: int, bet: Bet) -> str:
    """Play roulette."""

    slot: Slot = choice(ROULETTE)
    ctrl = globals()[f'bet_type_{bet.id}_ctrl']

    win = ctrl(person=person, bet=bet, amount=amount, slot=slot)

    if not win:
        person.balance -= amount

    return f"[{slot.number} {slot.color}] {person.name} has balance: {person.balance} €"

ROULETTE = [set_slot(item) for item in range(0, 37)]
BETS = init_bets()
