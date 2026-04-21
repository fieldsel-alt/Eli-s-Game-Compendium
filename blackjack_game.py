from card_basics.cards_class import Card
from card_basics.deck import Deck
from typing import Optional

class Blackjack:
    def __init__(self) -> None:
        self._deck: Deck = Deck()
        self._deck.shuffle_deck()
        self._balance: int = 1500
        self._hand: list[Card] = []
        self._dealer_hand: list[Card] = []
        self._handsize: int = 2
        self._hand_sum: int = 0
        self._folded: bool = False
        self._dealer_sum: int = 0
        self._victory: Optional[bool] = None
        self._blackjack: bool = False

    def _calculate_total(self, hand: list[Card]) -> int:
        """FIXED: Unified Ace-handling logic to prevent sum mismatches."""
        total = sum(card.get_value() for card in hand)
        ace_count = sum(1 for card in hand if card.get_rank() == 0)
        while total <= 11 and ace_count > 0:
            total += 10
            ace_count -= 1
        return total

    def play(self) -> None:
        self.deal_hand()
        input("Press Enter to continue...")
        self.prompt_options()
        if not self._folded and not self.lost():
            self.eval_dealer()
        else:
            self._victory = False
            print(f"Game over. Your total: {self._hand_sum}")

    def print_hand(self, hands: list[Card], name: str) -> None:
        print(f'\n----{name} Hand:----')
        for card in hands:
            print(card.name_of_card())
        print('--------------')

    def deal_hand(self) -> None:
        for _ in range(self._handsize):
            self._hand.append(self._deck.draw_card())
            self._dealer_hand.append(self._deck.draw_card())
        self.update_hand_sum()
        self.print_hand(self._hand, 'Your')
        # Displaying second card of dealer
        print(f"\n--Dealer Hand:-- \n{self._dealer_hand[1].name_of_card()} \n??? of ???\n----------------")

    def update_hand_sum(self) -> None:
        self._hand_sum = self._calculate_total(self._hand)

    def lost(self) -> bool:
        return self._calculate_total(self._hand) > 21

    def prompt_options(self) -> None:
        playing = True
        while not self.lost() and playing:
            self.update_hand_sum()
            print(f'--Current Hand Sum: {self._hand_sum}--')

            if self._hand_sum == 21 and len(self._hand) == 2:
                print("!!!BLACKJACK!!!")
                self._blackjack = True
                break

            option = input('Do you want to: \n1. Hit \n2. Stay \n3. Fold\n ').lower()
            if option in ['1', 'one', 'hit', 'draw']:
                card = self._deck.draw_card()
                self._hand.append(card)
                print(f'\nYou drew: {card.name_of_card()}')
                self.print_hand(self._hand, 'Your')
                input("Press Enter to continue...")
            elif option in ['2', 'two', 'stay', 'stop']:
                playing = False
            elif option in ['3', 'three', 'fold', 'give up']:
                self._folded = True
                playing = False
            else:
                print("Invalid input. Type 1, 2, or 3.")

    def eval_dealer(self) -> None:
        print("\nDealer reveals hidden card...")
        self.print_hand(self._dealer_hand, "Dealer's")
        
        self._dealer_sum = self._calculate_total(self._dealer_hand)
        
        while self._dealer_sum < 17:
            card = self._deck.draw_card()
            self._dealer_hand.append(card)
            self._dealer_sum = self._calculate_total(self._dealer_hand)
            print(f"\nDealer draws: {card.name_of_card()}")
            print(f"--Dealer Hand Sum: {self._dealer_sum}--")
            input("Press Enter to continue...")

        # Determination Logic
        if self._blackjack:
            self._victory = True
        elif self._dealer_sum > 21 or self._hand_sum > self._dealer_sum:
            self._victory = True
        elif self._hand_sum == self._dealer_sum:
            self._victory = None
        else:
            self._victory = False

        if self._victory is True:
            print("You win!")
        elif self._victory is None:
            print("Push (tie).")
        else:
            print("Dealer wins.")

    def get_bj(self) -> bool:
        return self._blackjack

    def get_victory(self) -> Optional[bool]:
        return self._victory
