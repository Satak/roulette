"""
    Simple roulette game to test typing in Python with MyPy.
"""

from random import randint
from collections import namedtuple
from typing import List, NamedTuple, Dict

Color: NamedTuple = namedtuple('Color', ['value'])

class Person:
    """Person class."""

    def __init__(self, name: str, balance: int) -> None:
        self.name: str = name
        self.balance: int = balance

    def ask_color(self) -> Color:
        """Asks what color to bet."""

        return Color(value='RED' if bool(input('Choose RED=Any key, BLACK=Enter: ')) else 'BLACK')

    def ask_bet(self) -> int:
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

def get_roulette_color(num: int) -> Color:
    """Roulette colors."""

    blacks: List[int] = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

    if num in blacks:
        return Color(value='BLACK')
    elif num == 0:
        return Color(value='WHITE')
    else:
        return Color(value='RED')

def spin_roulette(person: Person, amount: int, color: Color) -> str:
    """Play roulette."""

    res: Color = ROULETTE.get(randint(0, 36))
    if res.value == color.value:
        person.balance += 2 * amount
    else:
        person.balance -= amount

    return f"[{res.value}] {person.name} has balance: {person.balance} €"

def main() -> None:
    """Main."""

    name: str = input('Give name: ')
    person: Person = Person(name=name, balance=100)

    while person.balance > 0:
        res: str = spin_roulette(
            person=person,
            amount=person.ask_bet(),
            color=person.ask_color()
        )
        print(res)

ROULETTE: Dict = {item: get_roulette_color(item) for item in range(0, 37)}

if __name__ == '__main__':
    main()
