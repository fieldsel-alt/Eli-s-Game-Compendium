from blackjack_game import Blackjack
from scoundrel import Scoundrel

def print_opening() -> None:
    print ("""
    =================================
    ||                             ||
    ||   Welcome to Eli's Awesome  ||
    ||                             ||
    ||       GAME COMPENDIUM       ||
    ||                             ||
    =================================
    """)

def print_games() -> None:
    game_list = ['Blackjack', 'Scoundrel']
    for index, game in enumerate(game_list):
        print(f'{index+1}.) {game}')

def scoundrel_func() -> None:
    Scoundrel().play()

def blackjack_func() -> None:
    turns = 0
    balance = 1500.0
    high_balance = 1500.0
    
    while balance > 0:
        print(f'\nCurrent Balance: ${balance}')
        try:
            wager_input = input("How much do you wager? $")
            wager = int(wager_input)
            if wager < 1 or wager > balance:
                print(f"Please wager between $1 and ${balance}")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        
        game = Blackjack()
        turns += 1
        game.play()
        
        # Calculate result
        result = game.get_victory()
        if result is True:
            reward = wager * 1.5 if game.get_bj() else wager
            balance += reward
            print(f"Winner! +${reward}")
        elif result is False:
            balance -= wager
            print(f"Lost! -${wager}")
        else:
            print("Push. Wager returned.")
        
        if balance > high_balance: high_balance = balance
        input('Press Enter to continue...')
    
    print(f'\nGame Over! Hands: {turns}. Peak Balance: ${high_balance}.')

def main() -> None:
    print_opening()
    # FIXED: Using a dictionary for game selection
    game_map = {
        '1': blackjack_func, 'bj': blackjack_func, 'blackjack': blackjack_func,
        '2': scoundrel_func, 'sc': scoundrel_func, 'scoundrel': scoundrel_func
    }
        
    while True:
        print_games()
        choice = input("\nWhat Game Would You Like To Play? ").lower()
        
        if choice in game_map:
            game_map[choice]()
        else:
            print("Selection not recognized.")
        
        play_again = input("\nReturn to Compendium Menu? (y/n): ").lower()
        if play_again not in ['y', 'yes', '1']:
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    main()
