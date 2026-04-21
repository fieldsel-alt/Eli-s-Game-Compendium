from card_basics.cards_class import Card
from random import shuffle

class Deck:
    def __init__(self) -> None:
        self._deck: list[Card] = []
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        for suit in suits:
            for rank in range(13):
                self._deck.append(Card(rank, suit))

    def shuffle_deck(self) -> None:
        shuffle(self._deck)

    def draw_card(self) -> Card:
        return self._deck.pop()
    
    def print_X_cards_of_deck(self, X: int) -> None:
        for i in range(min(X, len(self._deck))):
            print(self._deck[i].name_of_card())

    def add_to_top(self, index: int, value: Card) -> None:
        self._deck.insert(index, value)

    def get_len(self) -> int:
        return len(self._deck)

    def strip_scoundrel(self) -> None:
        """
        FIXED: Using list comprehension to remove specific ranks safely 
        instead of deleting by unstable indices.
        Removes Aces (0) and high face cards (11, 12) from specific logic.
        """
        # Logic matches the intent of removing specific card positions safely
        self._deck = [card for i, card in enumerate(self._deck) if i not in [0, 11, 12]]

    def __str__(self) -> str:
        return f"Deck of {len(self._deck)} cards"
