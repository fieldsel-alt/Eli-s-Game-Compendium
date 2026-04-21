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
        self._heal_bonus: int = 0
        self._dura_bonus: int = 0
        self._cursed: bool = False
        self._on_fire: int = 0

        self._shuffled_last_turn: bool = False



    def _add_monsters_to_deck(self, count: int) -> None:
        """Creates new monster cards and shuffles them into the deck."""
        monster_suits = ["Clubs", "Spades"]
    
        for _ in range(count):
            # Generate a random rank (1-10 to stay within standard monster values)
            rank = random.randint(1, 10)
            suit = random.choice(monster_suits)
        
            # Create the new card (not a Joker)
            new_monster = Card(rank, suit, is_joker=False)
        
            # Add to the deck (using index 0 for the top)
            self._deck.add_to_top(0, new_monster)
    
        # Shuffle so the player doesn't know exactly where the reinforcements are
        self._deck.shuffle_deck()
    def message(self, prompt: str) -> None:
        m_easy_list = [
                'A goblin leaps from the shadows!',
                'Rats swarm the chamber!',
                'An acidic ooze charges you!',
                'A monster attacks!',
                'A wild beast decides you\'re its next meal!',
                'You have disturbed an enspecially large hive!'
                ]
        m_medium_list = [
                 'A skeleton emerges from its grave!',
                  'A mimic forgoes its disguise!',
                  'A giant spider drops from the ceiling',
                  'A reanimated corpse draws its sword!',
                  'Briny tentacles burst through the walls!',
                  'A horde of devilish imps charge you!',
                  'A ghostly visage appears in front of you!',
                  'An ogre decides you are a worthy challenger!'
                  ]
        m_hard_list = [
                    'Your own shadow begins to rebel!',
                    'An unseen assasin presses their knife to your throat!',
                    'A divine light begins to burn your flesh',
                    'You happen upon a lich\'s phylactery, your intrusion is noticed.',
                    'The chamber walls sprout eyes, limbs, and mouths. You are surrounded!',
                    'An abnormally large Cyclops decides you look especially delicous!'
                        ]

        h_hard_list = [
                    f'You happen across another adventurer, you share some stories and a meal.',
                    f'A large feast sits on a banquet table. You help yourself.',
                    f'A glowing pool sits in the corner of this room. You cautiosly dip in.',
                    f'A strange green mist is thick in the air. As you inhale your health is replenished.',
                    f'A strange person charges you with a needle. Your wounds begin to close before your eyes.',
                    f'An armless hand grips a leather flask. You pour the contents of the flask onto your wounds.'
                    ]
        h_easy_list = [
                    f'You grab a red tonic sitting on a shelf.',
                    f'Strange herbs grow in the corner of the chamber. Their bitter taste reminds you of their medicinal nature.',
                    f'A forgotten backpack spills onto the floor. Expired salves, once hidden inside, replenish you.',
                    f'Intruding roots poke through the roof, although they have unpleasant flavor you feel your energy return.',
                    f'You discover a small loft hidden in a chamber. You rest for a mere moment.'
                    ]

        w_medium_list = ['A simple shortsword lies on the ground, it may prove useful.',
                  'An axe is hanging on a rack, it might improve your odds.',
                  'A spear is lodged into the skull of an unlucky adventurer, it may help you avoid sharing their fate.',
                  'A bloody room houses a longbow and a few arrows, hopefully you can put them to better use.'
                  ]
        w_hard_list = [
                    'A gilded broadsword leans against the wall, it thirsts for blood.',
                    'A large hammer glints inside of a nerby chest, it will serve you well.',
                    'In the middle of the room a crossbow sits upon a pedastol, it will pierce any fiend you happen upon.',
                    'A shield is mounted on the wall, the blades embedded in its edges will surely slice through any opponent.'
                ]

        w_easy_list = [
                    'A bloodied dagger lies on a table, you hope it isn\'t cursed.',
                    'You find a large brick dislodged from the wall, it will have to do.',
                    'A broken sword lays on the ground, it was clearly discarded by someone more fortunate.',
                    'A crude club is laid next to a slain ogre, it won\'t mind if you help yourself.'

                ]

        if prompt == 'm_h':
            print(random.choice(m_hard_list))
        elif prompt == 'm_m':
            print(random.choice(m_medium_list))
        elif prompt == 'm_e':
            print(random.choice(m_easy_list))
        elif prompt == 'h_h':
            print(random.choice(h_hard_list))
        elif prompt == 'h_e':
            print(random.choice(h_easy_list))
        elif prompt == 'w_h':
            print(random.choice(w_hard_list))
        elif prompt == 'w_m' :
            print(random.choice(w_medium_list))
        elif prompt == 'w_e':
            print(random.choice(w_easy_list))
        else:
            print('HEY PASS AN ACTUAL ARGUMENT!')


    def _handle_joker(self, card: Card) -> None:
        """Handles random outcomes for Joker cards."""
        event = -1
        if card.get_suit() in ['Hearts','Diamonds']:
            event = random.randint(0,3)

            if event == 0:
                
                print("""
                The Goddess T\'lupina blesses you.
                Your maximum health has increased by 5
                """)
                
                self._max_health += 5

                
            elif event == 1:
                
                print("""
                Before you enter the room you feel a sweltering heat.
                As you push open the door you see in front of you
                the blade of Tvell. It sits embedded in stone,
                you grab the handle and feel immeasurable power!
                """)
                
                
                self._durability = 20
                self._equipped = True
                
            elif event == 2:
                print("""
                All weapons have 2 more durability.
                """)
                self._dura_bonus += 2

            else:
                
                print("""
                You see a small shack in the middle of the enormous
                room. A man in medical garb walks out and greets you.
                He treats you with a nice meal and brews you a strange tea.
                It has a rancid taste and you feel the effects immediately.
                Whenever you heal you heal 3 more life.
                """)
                
                self._heal_bonus += 3

        if card.get_suit() in ['Spades','Clubs']:
            event = random.randint(0,3)

            if event == 0:
                
                print("""
                A shudder runs up your spine, you feel watched.
                Unger's dark eye appears before you.
                Manacles of shadow manifest around your ankles.
                You no longer can run from chambers.
                """)
                
                self._cursed = True
            elif event == 1:
                
                print("""As you step in the room the stone you step on
                slides down ever slightly. Spears shoot out of the walls
                digging into your flesh as you hurry out.
                You lose half of your life.""")
                
                self._health = self._health//2

            elif event == 2:
                print("""
                As you walk into the room you ignorantly trip a wire.
                Alarm bells ring, alerting all kinds of nasty critters
                of your presence. Three monsters enter the dungeon.
                """)

                self._add_monsters_to_deck(3)
            
            else:
                print("""
                You are engulfed in flames!
                """)
                self._on_fire = 3


                
        input("\nPress Enter to continue...\n")

    def perform_actions(self, choice: int) -> None:
        chosen = self._row.pop(choice - 1)
        if self._on_fire > 0:
            print("\nFlames kiss your flesh.")
            print(f"You are on fire for {self._on_fire - 1} more turns.\n")
            self._health -= self._on_fire
            self._on_fire -= 1
        
        # TRIGGER JOKER LOGIC
        if chosen.is_joker():
            self._handle_joker(chosen)
            return # Skip standard card logic

        if chosen.get_suit() == "Hearts":
            self._health += chosen.get_value_face() + self._heal_bonus

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
            self._durability = self._equip_value + self._dura_bonus
            self._equipped = True

            if self._equip_value <= 4:
                self.message('w_e')
            elif self._equip_value >= 11:
                self.message('w_h')
            else:
                self.message('w_m')

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
                        if self._cursed:
                            print("Unger's foul curse prevents you from running away.")
                        else:
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
                    elif shuffle_input == 'debug_omniscience':

                        print("\n--- OMNISCIENCE: REVEALING ALL REMAINING ROOMS ---")
                        # We access the private list inside the Deck object
                        # We use [::-1] because pop() takes from the end of the list (the "top")
                        remaining_cards = self._deck._deck[::-1] 
                        
                        for i, card in enumerate(remaining_cards, start=1):
                            print(f"Room {i}: {card.name_of_card()} ({card.card_type()})")
                        
                        print("--- END OF REVEAL ---\n")

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


