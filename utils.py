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
    
