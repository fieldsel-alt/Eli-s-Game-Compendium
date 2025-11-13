from card_basics.cards_class import Card
from card_basics.deck import Deck
import random
class Scoundrel:

    def __init__(self) -> None:

        self._deck = Deck()
        self._deck.strip_scoundrel()
        
        self._deck.shuffle_deck()
       
        self._row: list[Card] = []

        self._health: int = 20

        self._equip_value: int = 0
        self._durability: int = 0
        self._equipped: bool = False

        self._shuffled_last_turn: bool = False


    
    def message(self, prompt: str) -> None:

        m_list = ['A goblin leaps from the shadows!',
                'An acidic ooze charges you!',
                'A skeleton emerges from it\'s grave!',
                'A mimic forgoes it\'s disguise!',
                'A giant spider drops from the ceiling',
                'A reanimated corpse draws it\'s sword!',
                'A monster attacks!']
            
        h_list = [f"A red tonic sits on a shelf. You drink it; your health is replenished to {self._health}.",
                f'A large feasts sits on a banquet table. You help your self; your health is replensihed to {self._health}.',
                f'You spy a glowing pool in the corner of this room. You dip your hand in; your health is replenished to {self._health}.',
                f'A strange green mist is thick in the air. Your health is replenished to {self._health}.']

        w_list = ['A simple sword lies on the ground, it may prove useful.',
                'An axe is hanging on a rack, it might improve your odds.',
                'A spear is lodged into the skull of an unlucky adventurer, it may help you avoid sharing their fate.',
                'A bloodied dagger lies on a table, you hope it isn\'t cursed.',
                'A broadsword leans against the wall, it has seen better and worse days.']
            
        if prompt == 'm':
            print(random.choice(m_list))
        elif prompt == 'h':
            print(random.choice(h_list))
        elif prompt == 'w':
            print(random.choice(w_list))
        else:
            print('HEY DUMBASS PASS AN ACTUAL ARGUMENT (message function in scoundrel.py) ')

    def perform_actions(self, choice: int) -> None:
        chosen = self._row.pop(choice - 1)

        # Healing action
        if chosen.get_suit() == "Hearts":
            self._health += chosen.get_value_face()
            if self._health > 20:
                self._health = 20
                print('You can\t help but feel as though you may waste some excess.')
            self.message('h')

        # Equip weapon
        elif chosen.get_suit() == "Diamonds":
            self._equip_value = chosen.get_value_face()
            self._durability = self._equip_value
            self._equipped = True
            self.message('w')

        # Combat
        else:
            self.message('m')
            if self._equipped and self._durability >= chosen.get_value_face():
                self._durability = chosen.get_value_face()
                print(f"You smite the foul beast! Your weapon grows dull; it has {self._durability} power remaining.")
            else:
                self._health -= (chosen.get_value_face() - self._durability) 
                self._durability -= (chosen.get_value_face() - self._durability)
                if self._durability < 1:
                    self._durability = 0
                print(f"You are wounded! Without a strong weapon, your health is reduced to {self._health}.")

    def create_row(self) -> None:
        """Draw up to 4 cards in the chamber."""
        for _ in range(4 - len(self._row)):
            self._row.append(self._deck.draw_card())

    def shuffle_row(self) -> None:
        """Return all current cards to the deck and reshuffle."""
        while self._row:
            card = self._row.pop()
            self._deck.add_to_top(0, card)  # Make sure your Deck has insert()
        self._deck.shuffle_deck()

    def print_chamber(self) -> None:

        print("\nThe chamber contains:")
        for i, card in enumerate(self._row, start=1):
            print(f"{i}. {card.name_of_card()} ({card.card_type()})")
            
        if self._equipped:                
            print(f'Your weapon has {self._durability} power left.')
        else:
            print(f'You are unarmed.')
        print(f'You have {self._health} health.')




    def chamber_loopable(self) -> None:
        while not self._shuffled_last_turn and len(self._row) > 1:
                
            self.print_chamber()

            try:
                choice = int(input("Which room do you enter first? "))
                if 1 <= choice <= len(self._row):
                    self.perform_actions(choice)
                else:
                    print("Please choose a valid room, adventurer.")
            except ValueError:
                print("I do not understand, enter the number of the room you wish to enter.")

            if self._health <= 0:
                print("\nYou have perished in the dungeon...")
                return

            
    def tutorial(self) -> None:
        print("\nWelcome to Scoundrel!")
        print('Diamonds are weapons, hearts are healing')
        print('and the rest are monsters. Your weapons will degrade')
        print('with monster attacks. Empty the deck of chambers to win.')
        # WIP better explanation


    def main_options(self) -> None:
        while self._deck.get_len() > 0 and self._health > 0:
            active = True
            self.create_row()
            self.print_chamber()

            while active:
                shuffle_input = input("\n --- Do you want to move to another chamber? (You may only do this every other turn.) ").lower()

                if self._shuffled_last_turn:
                    print("You fled last turn! You muster your courage and enter the chamber unchanged.")
                    self._shuffled_last_turn = False
                    active = False
                elif shuffle_input in ['yes', 'y', '1']:
                    print("This chamber is too perilous. You turn the corner hoping for better luck.")
                    self.shuffle_row()
                    self._shuffled_last_turn = True
                    active = False
                elif shuffle_input in ['no','n','0']:
                    print("You steel your nerves and enter the chamber unchanged.")
                    self._shuffled_last_turn = False
                    active = False
                else:
                    print('I do not understand, try again.')

            self.chamber_loopable
        
        print("\nThe dungeon grows quiet. You have survived your journey!")

                
    def play(self) -> None:
        self.tutorial()
        self.main_options()
 
