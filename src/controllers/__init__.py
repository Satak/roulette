"""Controllers for all bet types."""

from models import Person, Bet, Slot

def bet_type_1_ctrl(person: Person, bet: Bet, amount: int, slot: Slot) -> bool:
    """Straight-up Controller"""
    number = person.ask_number()
    if slot.number == number:
        person.balance += bet.pay * amount
        return True

def bet_type_2_ctrl(person: Person, bet: Bet, amount: int, slot: Slot) -> bool:
    """Red or Black Controller"""
    color = person.ask_color()
    if slot.color == color.value:
        person.balance += bet.pay * amount
        return True

def bet_type_3_ctrl(person: Person, bet: Bet, amount: int, slot: Slot) -> bool:
    """Odd or Even Controller"""

    slot_is_even = slot.number % 2 == 0
    user_is_even = person.ask_odd_or_event() % 2 == 0

    if user_is_even == slot_is_even:
        person.balance += bet.pay * amount
        return True
