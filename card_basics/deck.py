from card_basics.cards_class import Card
from random import shuffle
import random # Add this import at the top


class Deck:
    def __init__(self) -> None:
        self._deck: list[Card] = []
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        for suit in suits:
            for rank in range(13):
                # 1% chance for each card to become a Joker
                is_joker = random.random() < 0.04 # 4%
                self._deck.append(Card(rank, suit, is_joker))
    
    # ... keep the rest of the Deck methods the same ...
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

        # Inside your Deck class in deck.py
    def remove_specific_cards(self, suit_name: str, count: int) -> None:
        """
        Filters out a specific number of cards of a given suit.
        """
        new_deck = []
        removed_count = 0
        
        # Iterate through the current internal list
        for card in self._deck:
            if card.get_suit() == suit_name and removed_count < count:
                removed_count += 1
                continue  # Do not add to the new list
            new_deck.append(card)
        
        # Replace the old list with the filtered one
        self._deck = new_deck
        self.shuffle_deck()
