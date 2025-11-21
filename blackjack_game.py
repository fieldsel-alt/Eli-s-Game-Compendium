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
        self._blackjack: bool = True

    def play(self) -> None:
        self.deal_hand()
        self.prompt_options()
        self.eval_dealer()
    
    def print_hand(self,hands: list[Card],name: str) -> None:
        print (f'\n----{name} Hand:----')
        for card in hands:
            print(card.name_of_card())
        print('--------------')
        
    
    def deal_hand(self) -> None:
        for i in range(self._handsize):
            self._hand.append(self._deck.draw_card())
            self._dealer_hand.append(self._deck.draw_card())
        self.print_hand(self._hand,'Your')
        print(f"\n--Dealer Hand:-- \n{self._dealer_hand[1].name_of_card()} \n??? of ???\n----------------")
    
    def lost(self) -> bool:

        self._hand_sum = 0
        ace_count = 0
        for card in self._hand:
            if card.get_value() == 1:
                ace_count += 1
            
            self._hand_sum += card.get_value()

        
        while self._hand_sum  <= 11 and ace_count > 0:
            self._hand_sum += 10
            ace_count -= 1

        if self._hand_sum > 21:
            return True
        else:
            return False

    def prompt_options(self) -> None:
        playing = True


        while not self.lost() and playing:
            print(f'--Current Hand Sum: {self._hand_sum}--')

            # Detects Blackjack
            if self._hand_sum == 21 and len(self._hand) == 2:
                print("!!!BLACKJACK!!!")
                self._blackjack = True
                playing = False

            #Option prompting
            option = input('Do you want to: \n1. Hit \n2. Stay \n3. Fold\n ')
            try:
                if option.lower() in ['1','one','hit','draw']:
                    self._hand.append(self._deck.draw_card())
                    print(f'Drew {self._hand[-1].name_of_card()}\n')
                elif option.lower() in ['2','two','stay','stop']:
                    playing = False
                elif option.lower() in ['3','three','fold','give up']:
                    playing = False
                    self._folded = True
                else:
                    print("I don't understand. Type 1, 2, or 3.")

            except:
                print('Please type one of the options given. (1, 2, or 3)')

        #Prints final layout/stats
        if not playing:
            self.lost()
            self.print_hand(self._hand,'Your')
            print(f'--Current Hand Sum: {self._hand_sum}--')
    
    def get_bj(self) -> bool:
        return self._blackjack
    

    def dealer_lost(self) -> bool:
        self._dealer_sum = 0
        ace_count = 0

        #ace detection
        for card in self._dealer_hand:
            if card.get_value() == 1:
                ace_count += 1
            
            self._dealer_sum += card.get_value()

        while self._dealer_sum  <= 11 and ace_count > 0:
            self._dealer_sum += 10
            ace_count -= 1
        
        # checks if dealer bust
        if self._dealer_sum > 21:
            return True
        else:
            return False

    def eval_dealer(self) -> None:
        
        dealer_total = 0
        aces = 0

        # ace detection
        for card in self._dealer_hand:
            dealer_total += card.get_value()
            if card.get_rank() == 0:
                aces += 1
        while dealer_total > 21 and aces:
            dealer_total -= 10
            aces -= 1
        
        # dealer play mechanics
        while dealer_total < 17:
            card = self._deck.draw_card()
            self._dealer_hand.append(card)
            print("\nDealer draws:", card.name_of_card())

            self.print_hand(self._dealer_hand,'Dealer\'s')
            dealer_total += card.get_value()
            print(f'--Current Hand Sum: {dealer_total}--')

            if card.get_rank() == 0:
                aces += 1
            while dealer_total > 21 and aces:
                dealer_total -= 10
                aces -= 1
        

        self._dealer_sum = dealer_total

        if self._blackjack:
            self._victory = True
        elif self._folded or self.lost():
            self._victory = False
        elif dealer_total > 21:
            self._victory = True
        elif self._hand_sum > dealer_total:
            self._victory = True
        elif self._hand_sum == dealer_total:
            self._victory = None
        else:
            self._victory = False

    
        self.print_hand(self._dealer_hand,'Dealer\'s Final')
        print("\nDealer total:", self._dealer_sum)
        print("Your total:", self._hand_sum)

        if self._victory is True:
            print("You win!")
        elif self._victory is None:
            print("Push (tie).")
        else:
            print("Dealer wins.")
        
    def get_victory(self) -> Optional[bool]:
        return self._victory

