from card_basics.cards_class import Card
from card_basics.deck import Deck

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

    def perform_actions(self, choice: int) -> None:
        chosen = self._row.pop(choice - 1)

        # Healing action
        if chosen.get_suit() == "Hearts":
            self._health += chosen.get_value_face()
            if self._health > 20:
                self._health = 20
                print('You can\t help but feel as though you may waste some excess.')
            print(f"A red tonic sits on a shelf. You drink it; replenishing your health to {self._health}.")

        # Equip weapon
        elif chosen.get_suit() == "Diamonds":
            self._equip_value = chosen.get_value_face()
            self._durability = self._equip_value
            self._equipped = True
            print("A useful weapon lies here. It may prove invaluable.")

        # Combat
        else:
            print("A monster attacks!")
            if self._equipped and self._durability >= chosen.get_value_face():
                self._durability = chosen.get_value_face()
                print(f"You smite the foul beast! Your blade grows dull; it may only smite monsters with {self._durability} power.")
            else:
                self._health -= chosen.get_value_face()
                print(f"You are wounded! Without a strong enough blade, your health is reduced to {self._health}.")

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

    def main_loopable(self) -> None:
        shuffled_last_turn = False
        print("\nWelcome to Scoundrel!")
        print('Diamonds are weapons, hearts are health potions')
        print('and the rest are monsters. Your weapons will degrade')
        print('with monster attacks. Empty the deck of chambers to win.')

        while self._deck.get_len() > 0 and self._health > 0:
            self.create_row()

            print("\nThe chamber contains:")
            for i, card in enumerate(self._row, start=1):
                print(f"{i}. {card.name_of_card()}")

            shuffle_input = input("\nDo you want to move to another chamber? (You may only do this every other turn.) ").lower()

            if shuffled_last_turn:
                print("You fled last turn! You muster your courage and enter the chamber unchanged.")
                shuffled_last_turn = False
            elif shuffle_input in ['yes', 'y', '1']:
                print("This chamber is too perilous. You turn the corner hoping for better luck.")
                self.shuffle_row()
                shuffled_last_turn = True
                continue
            else:
                print("You steel your nerves and enter the chamber unchanged.")
                shuffled_last_turn = False

            while not shuffled_last_turn and len(self._row) > 1:
                print("\nThe chamber contains:")
                for i, card in enumerate(self._row, start=1):
                    print(f"{i}. {card.name_of_card()}")

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

        print("\nThe dungeon grows quiet. You have survived your journey!")

    def play(self) -> None:
        self.main_loopable()

