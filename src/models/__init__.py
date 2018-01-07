"""models."""

from typing import List, NamedTuple
from collections import namedtuple

Color: NamedTuple = namedtuple('Color', ['value'])
Slot: NamedTuple = namedtuple('Slot', ['number', 'color'])
Bet: NamedTuple = namedtuple('Bet', ['id', 'name', 'pay'])

class Person:
    """Person class."""

    def __init__(self, name: str, balance: int) -> None:
        self.name: str = name
        self.balance: int = balance

    def ask_bet_type(self, bets: List[Bet]) -> Bet:
        """Ask user what to bet."""

        selection: int = int(input(f'Select bet {[bet.name for bet in bets]}: '))
        return bets[selection]

    def ask_color(self) -> Color:
        """Asks what color to bet."""

        return Color(value='RED' if bool(input('Choose RED=Any key, BLACK=Enter: ')) else 'BLACK')

    def ask_odd_or_event(self) -> int:
        """Ask odd or even."""

        return int(input(f'Choose odd or even: '))

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
