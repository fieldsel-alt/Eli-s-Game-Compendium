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
        self._max_health: int = 20
        self._equip_value: int = 0
        self._durability: int = 0
        self._equipped: bool = False

        self._shuffled_last_turn: bool = False

    def message(self, prompt: str) -> None:
        m_easy_list = [
                'A goblin leaps from the shadows!',
                'Rats swarm the chamber!',
                'An acidic ooze charges you!',
                'A monster attacks!',
                'A wild beast decides you\'re its next meal!'
                ]
        m_medium_list = [
                 'A skeleton emerges from its grave!',
                  'A mimic forgoes its disguise!',
                  'A giant spider drops from the ceiling',
                  'A reanimated corpse draws its sword!',
                  'Briny tentacles burst through the walls!',
                  'A horde of devilish imps charge you!',
                  'A ghostly visage appears in front of you!'
                  ]
        m_hard_list = [
                    'Your own shadow begins to rebel!',
                    'An unseen assasin presses their knife to your throat!',
                    'A divine light begins to burn your flesh',
                    'You happen upon a lich\'s phylactery, your intrusion is noticed.',
                    'The chamber walls sprout eyes, limbs, and mouths. You are surrounded!'
                        ]

        h_hard_list = [
                    f'You happen across another adventurer, you share stories and a meal. Your health is replensihed to {self._health}.',
                    f'A large feast sits on a banquet table. You help yourself; your health is replenished to {self._health}.',
                    f'A glowing pool sits in the corner of this room. You cautiosly dip in; your health is replenished to {self._health}.',
                    f'A strange green mist is thick in the air. As you inhale your health is replenished to {self._health}.',
                    f'A strange person charges you with a needle. As you are forcifully injected your health is replenished to {self._health}',
                    f'A bodiless hand sits next to a leather flask. You squeeze the contents of the flask onto your wounds; replenishing your health to {self._health}.'
                    ]
        h_easy_list = [
                    f'A red tonic sits on a shelf. You drink it; your health is replenseshied to {self._health}.'
                    f'Strange herbs grow in the corner of the chamber. Their bitter taste replenishes you to {self._health} health.',
                    f'A forsaken backpack spills onto the floor. Expired salves, once hidden inside, replenish you to {self._health}.',
                    f'Intruding roots poke through the roof, although they have unpleasant flavor they replenish you to {self._health}.}',
                    f'You discover a small loft hidden in a chamber. You rest for a mere moment replenishing your health to {self._health}.'
                    ]

        w_list = ['A simple shortsword lies on the ground, it may prove useful.',
                  'An axe is hanging on a rack, it might improve your odds.',
                  'A spear is lodged into the skull of an unlucky adventurer, it may help you avoid sharing their fate.',
                  'A bloodied dagger lies on a table, you hope it isn\'t cursed.',
                  'A broadsword leans against the wall, it has seen better and worse days.',
                  'A large hammer glints inside of a nearby chest, it will serve you well.']

        if prompt == 'm_h':
            print(random.choice(m_hard_list))
        elif prompt == 'm_m':
            print(random.choice(m_medium_list))
        elif prompt == 'm_e':
            print(random.choice(m_easy_list))
        elif prompt == 'h_h':
            print(random.choice(h_hard_list))
        elif prompt == 'h_e'
            print(random.choice(h_easy_list))
        elif prompt == 'w':
            print(random.choice(w_list))
        else:
            print('HEY PASS AN ACTUAL ARGUMENT!')

    def perform_actions(self, choice: int) -> None:
        chosen = self._row.pop(choice - 1)

        # Healing action
        if chosen.get_suit() == "Hearts":
            self._health += chosen.get_value_face()
            if self._health > self._max_health:
                self._health = self._max_health
                if chosen.get_value_face() > 8:
                    self.message('h_h')
                else:
                    self.message('h_e')
                print('You feel some excess energy go to waste.')
            else:
                if chosen.get_value_face() > 8:
                    self.message('h_h')
                else:
                    self.message('h_e')

            
            input("\nPress Enter to continue...\n ")

        # Equip weapon
        elif chosen.get_suit() == "Diamonds":
            self._equip_value = chosen.get_value_face()
            self._durability = self._equip_value
            self._equipped = True
            self.message('w')
            input("\nPress Enter to continue...\n ")

        # Combat
        else:
            monster_value = chosen.get_value_face()

            if monster_value <= 4:        #prints message based on strength of monster
                self.message('m_e')
            elif monster_value >= 11:
                self.message('m_h')
            else:
                self.message('m_m')

            if self._equipped and self._durability > 0:
                damage = min(monster_value, self._durability)
                self._durability -= damage
                leftover = monster_value - damage
                self._health -= leftover
                if self._health < 0:
                    self._health = 0
                print(f"You attack! Weapon durability: {self._durability}. Health: {self._health}.")
                input("\nPress Enter to continue... \n")
            else:
                self._health -= monster_value
                if self._health < 0:
                    self._health = 0
                print(f"You are attacked! Health reduced to {self._health}.")
                input("\nPress Enter to continue... \n")

    def create_row(self) -> None:
        """Draw up to 4 cards in the chamber."""
        for _ in range(4 - len(self._row)):
            self._row.append(self._deck.draw_card())

    def shuffle_row(self) -> None:
        """Return all current cards to the deck and reshuffle."""
        while self._row:
            card = self._row.pop()
            self._deck.add_to_top(0, card)
        self._deck.shuffle_deck()

    def print_chamber(self) -> None:
        print(f"\n{self._deck.get_len()} rooms remaining\nThe chamber contains:")
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
                choice = int(input(f"Which room do you enter first? "))
                if 1 <= choice <= len(self._row):
                    self.perform_actions(choice)
                else:
                    print("Please choose a valid room, adventurer.")
            except ValueError:
                print("Enter the number of the room you wish to enter.")

            if self._health <= 0:
                print("\nYou have perished in the dungeon...")
                return

    def tutorial(self) -> None:
        print("\nWelcome to Scoundrel!")
        print('Diamonds are weapons, hearts are healing, and the rest are monsters.')
        print('Your weapons degrade with monster attacks. Empty the deck of chambers to win.')
        input("\nPress Enter to continue...\n ")

    def main_options(self) -> None:
        while self._deck.get_len() > 0 and self._health > 0:
            self.create_row()         
            if not self._shuffled_last_turn:
                self.print_chamber()
                input("\nPress Enter to continue... \n")
            

            active = True
            while active:
                if self._shuffled_last_turn:
                    print("\nYou fled last turn. You enter the next chamber warily.")
                    self._shuffled_last_turn = False
                    active = False
                else:
                
                    shuffle_input = input("Do you want to move to another chamber? (You may only do this every other turn.) ")

                    if shuffle_input.lower() in ['yes', 'y']:
                        print("This chamber is too perilous. You turn the corner hoping for better luck.")
                        self.shuffle_row()
                        self._shuffled_last_turn = True
                        active = False
                    elif shuffle_input.lower() in ['no', 'n']:
                        print("You steel your nerves and enter the chamber unchanged.")
                        self._shuffled_last_turn = False
                        active = False
                    elif shuffle_input == "debug_god_mode":
                        self._equipped = True
                        self._max_health = 999999999
                        self._health = 999999999
                        self._durability = 999999999
                    elif shuffle_input == "debug_empty_chamber":
                        while self._deck.get_len() >= 4:
                            dump = []
                            dump.append(self._deck.draw_card())
                    else:
                        print('I do not understand, try again.')

            # Call the chamber loop properly
            self.chamber_loopable()
        if self._health > 0:
            print("\nThe dungeon grows quiet. You have survived your journey!")
        else:
            print('\n The dungeon grows ever louder. You have failed your journey. ')

    def play(self) -> None:
        self.tutorial()
        self.main_options()

