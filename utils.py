import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def dash_21():
    print("---------------------")


def press_enter_to_continue():
    input("Press Enter to continue...")


def lose(player, bet):
    player.adjust_balance(-bet)
    print("You lose!")
    dash_21()


def win(player, bet):
    player.adjust_balance(bet)
    print("You win!")
    dash_21()


def draw(player):
    print("It's a draw!")
    dash_21()


def game_intro(game_name):
    clear_screen()
    dash_21()
    print(f"Welcome to {game_name}!")
    dash_21()


def get_bet(player):
    while True:
        try:
            bet = int(input(f"{player.name}, you have ${player.balance}. Place your bet: "))
            if 1 <= bet <= player.balance:
                return bet
            print("Invalid bet.")
        except ValueError:
            print("Please enter a number.")
    
