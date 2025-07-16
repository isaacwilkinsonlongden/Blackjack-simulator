import time
from utils import clear_screen, dash_21, press_enter_to_continue, lose, win, draw
from cards import Deck
from player import Player


class BlackjackPlayer(Player):
    def __init__(self, name, balance=100):
        super().__init__(name, balance)
        self.hand = []

    def reset_hand(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        value = 0
        aces = 0

        for card in self.hand:
            if card.rank in ["J", "Q", "K"]:
                value += 10
            elif card.rank == "A":
                aces += 1
                value += 11
            else:
                value += int(card.rank)

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value
    
    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)


def play_blackjack(player):
    while True:
        clear_screen()
        dash_21()
        print("Welcome to Blackjack!")
        dash_21()

        bet = get_bet(player)
        deck = Deck()
        deck.shuffle()

        p = BlackjackPlayer(player.name, player.balance)
        dealer = BlackjackPlayer("Dealer")
        p.reset_hand()
        dealer.reset_hand()

        for _ in range(2):
            p.add_card(deck.deal_card())
            dealer.add_card(deck.deal_card())

        if player_turn(p, dealer, deck):
            show_results(p, dealer)
            lose(player, bet)
        elif dealer_turn(dealer, p, deck):
            show_results(p, dealer)
            win(player, bet)
        else:
            show_results(p, dealer)
            if p.get_hand_value() > dealer.get_hand_value():
                win(player, bet)
            elif p.get_hand_value() < dealer.get_hand_value():
                lose(player, bet)
            else:
                draw(player)

        play_again = input("Play another round? (y/n): ").strip().lower()
        if play_again not in ['y', 'yes']:
            return


def get_bet(player):
    while True:
        try:
            bet = int(input(f"{player.name}, you have ${player.balance}. Place your bet: "))
            if 1 <= bet <= player.balance:
                return bet
            print("Invalid bet.")
        except ValueError:
            print("Please enter a number.")


def player_turn(p, dealer, deck):
    while p.get_hand_value() <= 21:
        player_turn_show_hands(p, dealer)
        choice = input("Hit or stand? ").strip().lower()
        if choice in ["stand", "s"]:
            break
        elif choice in ["hit", "h"]:
            p.add_card(deck.deal_card())
    if p.get_hand_value() > 21:
        player_turn_show_hands(p, dealer)
        print("YOU BUSTED!")
        time.sleep(2)
        return True


def dealer_turn(dealer, p, deck):
    while dealer.get_hand_value() < 17:
        dealer_turn_show_hands(dealer, p)
        time.sleep(2)
        dealer.add_card(deck.deal_card())

    if dealer.get_hand_value() > 21:
        dealer_turn_show_hands(dealer, p)
        print("DEALER BUSTED!")
        time.sleep(2)
        return True
    
    dealer_turn_show_hands(dealer, p)
    time.sleep(2)


def show_results(p, dealer):
    clear_screen()
    print("--- Final Hands ---")
    print(f"Dealer: {dealer.show_hand()} ({dealer.get_hand_value()})")
    print(f"{p.name}: {p.show_hand()} ({p.get_hand_value()})")
    dash_21()


def player_turn_show_hands(p, dealer):
    clear_screen()
    dash_21()
    print(f"Dealer shows: {dealer.hand[0]} ?")
    dash_21()
    print(f"Your hand: {p.show_hand()} ({p.get_hand_value()})")
    dash_21()

def dealer_turn_show_hands(dealer, p):
    clear_screen()
    dash_21()
    print(f"Dealer's hand: {dealer.show_hand()} ({dealer.get_hand_value()})")
    dash_21()
    print(f"Your hand: {p.show_hand()} ({p.get_hand_value()})")
    dash_21()


        



            

        








        
