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

def ask_color() -> Color:
    """Asks color where to bet."""

    return Color(value='RED' if int(input('Choose RED=1, BLACK=0: ')) else 'BLACK')

def main() -> None:
    """Main."""

    name: str = input('Give name: ')
    person: Person = Person(name=name, balance=100)

    while person.balance > 0:
        amount: int = int(input('Give gamble amount: '))
        res: str = spin_roulette(person=person, amount=amount, color=ask_color())
        print(res)

ROULETTE: Dict = {item: get_roulette_color(item) for item in range(0, 37)}

if __name__ == '__main__':
    main()
