from card_basics.cards_class import Card
from random import shuffle

class Deck:
    def __init__(self) -> None:
        self._deck = []
        suits = ("Hearts","Diamonds","Clubs","Spades")
        for suit in suits:
            for rank in range(13):
                self._deck.append(Card(rank,suit))

    def shuffle_deck(self) -> None:
        shuffle(self._deck)

    def draw_card(self) -> Card:
        return self._deck.pop()
    
    def print_X_cards_of_deck(self, X:int) -> None:
        for i in range(0,X):
            card = self._deck[i]
            print(card.name_of_card())


                
                
