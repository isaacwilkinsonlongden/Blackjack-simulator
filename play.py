from main import *
import time

def play():
    while True:
        result = main()

        if result == "win":
            print("YOU WIN!")
        elif result == "lose":
            print("YOU LOSE!")
        else:
            print("YOU DRAW!")

        play_again = input("Play again? y/n: ").strip().lower()
        if play_again not in ("y", "yes"):
            print("-------------------")
            print("Thanks for playing!")
            print("-------------------")
            break


def main():
    deck = Deck()
    player_name = input("Enter your name: ")
    player = Player(player_name)
    dealer = Player("Dealer")

    deck.shuffle()

    for i in range(2):
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())

    print(f"Dealers hand: {dealer.hand[0]} ?")

    if player_turn(player, deck):
        return "lose"

    if dealer_turn(dealer, deck):
        return "win"
        
    if player.get_hand_value() > dealer.get_hand_value():
        return "win"
    elif player.get_hand_value() < dealer.get_hand_value():
        return "lose"
    else:
        return "draw"


def player_turn(player, deck):
    while player.get_hand_value() <= 21:
        print(player.show_hand())
        choice = input("Hit or Stand? ").strip().lower()

        if choice in ["hit", "h"]:
            player.add_card(deck.deal_card())
        elif choice in ["stand", "s"]:
            break

    if player.get_hand_value() > 21:
        return True
    

def dealer_turn(dealer, deck):
    while dealer.get_hand_value() < 17:
        print(dealer.show_hand())
        time.sleep(1)
        dealer.add_card(deck.deal_card())

    if dealer.get_hand_value() > 21:
        return True


if __name__ == "__main__":
    play()

        



            

        








        
