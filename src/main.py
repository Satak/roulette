"""
    Simple roulette game to test typing in Python with MyPy.
"""

from random import choice
from collections import namedtuple
from typing import List, NamedTuple

Color: NamedTuple = namedtuple('Color', ['value'])
Slot: NamedTuple = namedtuple('Slot', ['number', 'color'])
Bet: NamedTuple = namedtuple('Bet', ['name', 'pay'])

class Person:
    """Person class."""

    def __init__(self, name: str, balance: int) -> None:
        self.name: str = name
        self.balance: int = balance

    def ask_bet_type(self) -> Bet:
        """Ask user what to bet."""

        selection: int = int(input(f'Select bet {[bet.name for bet in BETS]}: '))
        return BETS[selection]

    def ask_color(self) -> Color:
        """Asks what color to bet."""

        return Color(value='RED' if bool(input('Choose RED=Any key, BLACK=Enter: ')) else 'BLACK')

    def ask_bet_amount(self) -> int:
        """
            Ask user how much he wants to gamble.

            Bet can't be a string, less than 0 or higher than your balance.
            If you press enter at the input it's all in.
        """
        user_input: str = ""
        while not user_input.isnumeric() or\
            int(user_input) > self.balance or\
            int(user_input) <= 0:

            user_input = str(input(f'Give gamble amount (max {self.balance} €) (Enter=All in): '))
            if user_input == '':
                user_input = str(self.balance)
        return int(user_input)

    def ask_number(self) -> int:
        """Ask what number to bet."""

        user_input: str = ""
        while not user_input.isnumeric() or\
            int(user_input) > 36 or\
            int(user_input) < 0:
            user_input = str(input(f'Give number to bet (0-36): '))

        return int(user_input)

def init_bets() -> List[Bet]:
    """Bet initializer."""

    bets = [
        {
            'name': 'Straight-up',
            'pay': 36
        },
        {
            'name': 'Red or Black',
            'pay': 2
        },
        {
            'name': 'Odd or Even',
            'pay': 2
        }
    ]

    return [Bet(**bet) for bet in bets]

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

    win = False
    res: Slot = choice(ROULETTE)
    print(res)
    if bet.name == 'Red or Black':
        color = person.ask_color()
        if res.color == color.value:
            person.balance += bet.pay * amount
            win = True
    elif bet.name == 'Straight-up':
        number = person.ask_number()
        if res.number == number:
            person.balance += bet.pay * amount
            win = True

    if not win:
        person.balance -= amount

    return f"[{res.number} {res.color}] {person.name} has balance: {person.balance} €"

def main() -> None:
    """Main."""

    name: str = input('Give name: ')
    person: Person = Person(name=name, balance=100)

    while person.balance > 0:
        res: str = spin_roulette(
            person=person,
            amount=person.ask_bet_amount(),
            bet=person.ask_bet_type()
        )
        print(res)

ROULETTE = [set_slot(item) for item in range(0, 37)]
BETS = init_bets()

if __name__ == '__main__':
    main()
