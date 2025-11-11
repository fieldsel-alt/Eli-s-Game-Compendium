class Card:
    def __init__(self, suit: int, rank: str) -> None:
        self._rank: int = suit
        self._suit: str = rank

    def name_of_card(self) -> str:
        if self._rank == 0:
            name_rank = "Ace"
        elif self._rank == 1:
            name_rank = "Two"
        elif self._rank == 2:
            name_rank = "Three"
        elif self._rank == 3:
            name_rank = "Four"
        elif self._rank == 4:
            name_rank = "Five"
        elif self._rank == 5:
            name_rank = "Six"
        elif self._rank == 6:
            name_rank = "Seven"
        elif self._rank == 7:
            name_rank = "Eight"
        elif self._rank == 8:
            name_rank = "Nine"
        elif self._rank == 9:
            name_rank = "Ten"
        elif self._rank == 10:
            name_rank = "Jack"
        elif self._rank == 11:
            name_rank = "Queen"
        elif self._rank == 12:
            name_rank = "King"
        else:
            name_rank = str(self._rank + 1)

        return f"{name_rank} of {self._suit}"

    def get_rank(self) -> int:
        return self._rank

    def get_suit(self) -> str:
        return self._suit

    def get_value(self) -> int:
        if self._rank < 9:
            return self._rank + 1
        else:
            return 10

    def get_value_face(self) -> int:
        if self._rank == 0:
            return 14
        else:
            return self._rank + 1
         

