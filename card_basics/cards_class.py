class Card:
    RANKS = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
             "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    def __init__(self, rank: int, suit: str, is_joker: bool = False) -> None:
        self._rank: int = rank
        self._suit: str = suit
        self._is_joker: bool = is_joker 

    def name_of_card(self) -> str:
        if self._is_joker:
            name_rank = 'Joker'
        elif 0 <= self._rank < len(self.RANKS):
            name_rank = self.RANKS[self._rank]
        else:
            name_rank = str(self._rank + 1)
        return f"{name_rank} of {self._suit}"

    def get_rank(self) -> int:
        return self._rank

    def get_suit(self) -> str:
        return self._suit

    def is_joker(self) -> bool:
        return self._is_joker

    def get_value(self) -> int:
        """Standard values for Blackjack."""
        if self._rank < 9:
            return self._rank + 1
        else:
            return 10

    def get_value_face(self) -> int:
        """Values for Scoundrel (Ace = 14)."""
        if self._rank == 0:
            return 14
        else:
            return self._rank + 1
    
    def card_type(self) -> str:
        if self._is_joker:
            return 'Mystery'
        if self._suit == 'Diamonds':
            return 'Weapon'
        elif self._suit == 'Hearts':
            return 'Healing'
        else:
            return 'Monster'
