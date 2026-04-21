class Card:
    # Use a class-level list for efficient rank mapping
    RANKS = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
             "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    def __init__(self, rank: int, suit: str) -> None:
        # FIXED: Corrected the swapped suit/rank assignment
        self._rank: int = rank
        self._suit: str = suit

    def name_of_card(self) -> str:
        # FIXED: Simplified lookup using list indexing
        if 0 <= self._rank < len(self.RANKS):
            name_rank = self.RANKS[self._rank]
        else:
            name_rank = str(self._rank + 1)
        return f"{name_rank} of {self._suit}"

    def get_rank(self) -> int:
        return self._rank

    def get_suit(self) -> str:
        return self._suit

    def get_value(self) -> int:
        """Standard values for Blackjack (Face cards = 10)."""
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
        if self._suit == 'Diamonds':
            return 'Weapon'
        if self._suit == 'Hearts':
            return 'Healing'
        else:
            return 'Monster'
