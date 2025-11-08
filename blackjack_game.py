from card_basics.cards_class import Card
from card_basics.deck import Deck

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

    def play(self) -> None:
        self.deal_hand()
        self.prompt_options()
    
    def print_hand(self,hands: list[Card]) -> None:
        print ('\n----Hand:----')
        for card in hands:
            print(card.name_of_card())
        print('--------------')
    
    def deal_hand(self) -> None:
        for i in range(self._handsize):
            self._hand.append(self._deck.draw_card())
            self._dealer_hand.append(self._deck.draw_card())
        self.print_hand(self._hand)
        print(f"\n--Dealer Hand:-- \n{self._dealer_hand[1].name_of_card()} \n??? of ???\n----------------")
    
    def lost(self) -> bool:

        self._hand_sum = 0
        ace_count = 0
        for card in self._hand:
            if card.get_rank() == 1:
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
            option = input('Do you want to: \n1. Hit \n2. Stay \n3. Fold\n ')
            try:
                if option.lower() in ['1','one','hit','draw']:
                    self._hand.append(self._deck.draw_card())
                elif option.lower() in ['2','two','stay','stop']:
                    playing = False
                elif option.lower() in ['3','three','fold','give up']:
                    playing = False
                    self._folded = True
                else:
                    print("I don't understand. Type 1, 2, or 3.")

            except:
                print('Please type one of the options given. (1, 2, or 3)')
