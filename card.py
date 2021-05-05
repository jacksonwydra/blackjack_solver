from enum import Enum
from typing import NewType


CardSuit = NewType('CardType', str)


class Card:
    def __init__(self, name: str, suit: CardSuit, value: int) -> None:
        self.name = name
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        return f'{self.name} of {self.suit.value} (Value: {self.value})'


class CardSuit(Enum):
    CLUBS = 'Clubs'
    DIAMONDS = 'Diamonds'
    HEARTS = 'Hearts'
    SPADES = 'Spades'
