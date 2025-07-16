import random
import time
from utils import clear_screen, dash_21, game_intro, get_bet


def play_slots(player):
    game_name = "Slots"
    game_intro(game_name)
    bet = get_bet(player)

    dash_21()
    input("Press Enter to spin the reels...")
    dash_21()

    while True:
        symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "💎"]
        reels = [random.choice(symbols) for _ in range(3)]

        player.adjust_balance(-bet)
        if len(set(reels)) == 1:
            spin(bet, player, reels, 10)
        elif len(set(reels)) == 2:
            spin(bet, player, reels, 5)
        else:
            spin(bet, player, reels, 0)

        play_again = input("Spin again/change bet? (y/n/b): ").strip().lower()
        if play_again == 'b':
            bet = get_bet(player)
        elif play_again not in ['y', 'yes']:
            break


def spin(bet, player, reels, multiplier=0):
    clear_screen()
    win_amount = bet * multiplier
    player.adjust_balance(win_amount)

    print("Spinning...")
    time.sleep(2)
    print(f"{" | ".join(reels)}")
    time.sleep(2)

    if multiplier == 10:
        print(f"Jackpot! You win ${win_amount}!")
    elif multiplier == 5:
        print(f"Great! You win ${win_amount}!")
    else:
        print("Unfortunately, you didn't win this time")
        
    print(f"\nYour new balance is ${player.balance}")

        



    
    
    