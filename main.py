from blackjack_game import Blackjack
from scoundrel import Scoundrel

def scoundrel_func() -> None:
    game_sc = Scoundrel()
    game_sc.play()

def blackjack_func() -> None:
    turns = 0
    balance:float = 1500
    high_balance:float = 1500
    print(f'Current Balance: ${balance}')
    
    while balance > 0:

        while True:
            try:
                wager = int(input("How much do you wager? $"))
                if wager < 1 or wager > balance:
                    raise ValueError
                break
            except:
                print("There was an error, write a whole positive integer that is less than your balance.")
        
        blackjack = Blackjack()
        turns += 1
        blackjack.play()
        
        if blackjack.get_victory() == True:
            if blackjack.get_bj():
                balance += (wager * 1.5)
            else:
                balance += wager
        elif blackjack.get_victory() == False:
            balance -= wager
        
        if balance > high_balance:
            high_balance = balance

        print(f'\nCurrent Balance: {balance}')
    
    print(f'You ran out of money, game over!\n You played {turns} hands.\n You had a maximum of ${high_balance}.')

def main() -> None:
    game_choice = input("Hwat Game? ")
    if game_choice.lower() in ['bj','b','black','black jack','blackjack']:
        blackjack_func()
    elif game_choice.lower() in ['sc','s','scoundrel']:
        scoundrel_func()
    else:
        print('idk')
if __name__ == '__main__':
    main()
