from card import Card, CardSuit


class BlackJackDeck:
    def __init__(self, num_of_decks: int) -> None:
        self.num_of_decks = num_of_decks
        self.cards = []

        self.create_deck()

    def create_deck(self):
        for i in range(self.num_of_decks):
            for suit in CardSuit:
                for i in range(2, 11):
                    self.cards.append(Card(str(i), suit, i))

                self.cards.append(Card("Jack", suit, 10))
                self.cards.append(Card("Queen", suit, 10))
                self.cards.append(Card("King", suit, 10))
                self.cards.append(Card("Ace", suit, 11))

    def shuffle_deck(self):
        pass

    def draw_card(self):
        pass
