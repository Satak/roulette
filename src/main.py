"""
    Simple roulette game to test typing in Python with MyPy.
"""

from models import Person
from utils import spin_roulette, BETS

def main() -> None:
    """Main."""

    name: str = input('Give name: ')
    person: Person = Person(name=name, balance=100)

    while person.balance > 0:
        res: str = spin_roulette(
            person=person,
            amount=person.ask_bet_amount(),
            bet=person.ask_bet_type(bets=BETS)
        )
        print(res)


if __name__ == '__main__':
    main()
