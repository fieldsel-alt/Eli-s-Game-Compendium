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

    def add_to_top(self,index: int, value: Card) -> None:
        self._deck.insert(index,value)

    def get_len(self) -> int:
        return(len(self._deck))

    def strip_scoundrel(self) -> None:
        del self._deck[11:13]
        del self._deck [0]

                
