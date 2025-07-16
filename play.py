from main import *
import time
import os

def play():
    while True:
        result = main()

        if result == "win":
            print("YOU WIN!")
        elif result == "lose":
            print("YOU LOSE!")
        else:
            print("YOU DRAW!")

        time.sleep(2)
        print("-------------------")
        play_again = input("Play again? y/n: ").strip().lower()
        if play_again not in ("y", "yes"):
            print("-------------------")
            print("Thanks for playing!")
            print("-------------------")
            break


def main():
    clear_screen()
    deck = Deck()
    player = Player("Player")
    dealer = Player("Dealer")

    deck.shuffle()

    for i in range(2):
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())

    if player_turn(player, dealer, deck):
        return "lose"

    if dealer_turn(dealer, player, deck):
        return "win"
        
    clear_screen()
    show_results(player, dealer)
    if player.get_hand_value() > dealer.get_hand_value():
        return "win"
    elif player.get_hand_value() < dealer.get_hand_value():
        return "lose"
    else:
        return "draw"
    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def player_turn(player, dealer, deck):
    while player.get_hand_value() <= 21:
        clear_screen()
        player_turn_show_hands(player, dealer)
        choice = input("Hit or Stand? ").strip().lower()

        if choice in ["hit", "h"]:
            player.add_card(deck.deal_card())
        elif choice in ["stand", "s"]:
            print("You stand.")
            time.sleep(1)
            break

    if player.get_hand_value() > 21:
        clear_screen()
        player_turn_show_hands(player, dealer)
        print("YOU BUSTED!")
        time.sleep(2)
        clear_screen()
        show_results(player, dealer)
        return True
    

def dealer_turn(dealer, player, deck):
    while dealer.get_hand_value() < 17:
        clear_screen()
        dealer_turn_show_hands(dealer, player)
        time.sleep(2)
        dealer.add_card(deck.deal_card())

    if dealer.get_hand_value() > 21:
        clear_screen()
        dealer_turn_show_hands(dealer, player)
        print("DEALER BUSTED!")
        time.sleep(2)
        clear_screen()
        show_results(player, dealer)
        return True

    clear_screen()
    dealer_turn_show_hands(dealer, player)
    time.sleep(2)
    

def show_results(player, dealer, pause=True):
    print("--- Final Hands ---")
    print(f"Dealer: {dealer.show_hand()} ({dealer.get_hand_value()})")
    print(f"{player.name}: {player.show_hand()} ({player.get_hand_value()})")
    print("-------------------")
    
    if pause:
        time.sleep(2)


def player_turn_show_hands(player, dealer):
    print("-------------------")
    print(f"Dealers hand: {dealer.hand[0]} ?")
    print("-------------------")
    print(f"Your hand: {player.show_hand()}")
    print("-------------------")


def dealer_turn_show_hands(dealer, player):
    print("-------------------")
    print(f"Dealers hand: {dealer.show_hand()}")
    print("-------------------")
    print(f"Your hand: {player.show_hand()}")
    print("-------------------")


if __name__ == "__main__":
    play()

        



            

        








        
