from card_basics.cards_class import Card
from card_basics.deck import Deck

class Scoundrel():

    def __init__(self) -> None:
        
        self._deck = Deck()
        self._deck.shuffle_deck()
        
        self._row: list[Card] = []
        
        self._health: int = 20

        self._equip_value:int = 0

        self._durability:int = 0

        self._equipped: bool = False

    def perform_actions(self, choice:int ) -> None:
        chosen = self._row.pop(choice-1)

        if chosen.get_suit() == "Hearts":
            self._health += chosen.get_value_face()
            if self._health > 20:
                self._health = 20
            print(f"A red tonic sit on a shelf. You drink it; replenishing your health to {self._health}")

        elif chosen.get_suit() == "Diamonds":
            self._equip_value = chosen.get_value_face()
            self._durability = self._equip_value
            self._equipped = True
            print('A useful weapon lies here. It may prove invaluable.')

        else:
            print('A monster attacks!')
            if self._equipped and self._durability >= chosen.get_value_face():
                self._durability = chosen.get_value_face()
                print('You smite the foul beast, your blade grows dull; it may only smite monsters with {self._durability} power.')
                
            else:
                self._health -= chosen.get_value_face()
                print(f'You smite the foul beast, without a strong enough blade you are reduced to {self._health} health.')
    
    def create_row(self) -> None:

        for i in range(4-len(self._row)):
            self._row.append(self._deck.draw_card())
    
    def shuffle_row(self) -> None:

        for i in range(4):
            self._deck.insert(0,self._row.pop())

    def main_loopable(self) -> None:
        while self._deck.get_len() > 0:

            self.create_row()
            shuffled = False

            i = 0
            print("The chamber contains:")
            for card in self._row:
                i += 1
                print(f'{i}. {card.name_of_card()}')
            
        
            active = True
            while active:
                try:
                    shuffle = input("Do you want to move to another chamber? (You may only do this every other turn.) ")
                    active = False
                except:
                    print("I do not understand, say yes or no.")
        
            if shuffled:
                print('You fled last turn! You muster your waning courage and enter the chamber unchanged. ')
                shuffled = False
            elif shuffle.lower() in ['yes','y','yuh','1']:
                print("This chamber is too perilous. You turn the corner hoping for better luck.")
                shuffled = True

            else:
                print('You steel your neves and enter the chamber unchanged.')
                shuffled = False

            while not shuffled and len(self._row) > 1:
            
                i = 0
                print("The chamber contains:")
                for card in self._row:
                    i += 1
                    print(f'{i}. {card.name_of_card()}')
            
                active = True
                while active:
                    try:
                        choice = int(input('Which room do you enter first? '))
                        if choice <= len(self._row):
                            active = False
                    except:
                        print('I do not understand, enter the nummber of the room you wish to enter. ')

                self.perform_actions(choice)


    def play(self) -> None:
        self.main_loopable()
