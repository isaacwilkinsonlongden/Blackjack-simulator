import time
from utils import clear_screen, dash_21, game_intro, press_enter_to_continue
from cards import Deck
from player import Player


class PokerPlayer(Player):
    def __init__(self, name, balance=100):
        super().__init__(name, balance)
        self.hole_cards = []
        self.in_hand = True

    def deal_hole_cards(self, cards):
        self.hole_cards = cards

    def show_hand(self, hide=False):
        if hide:
            return "?? ??"
        return ' '.join(str(card) for card in self.hole_cards)
    

def play_poker(player):
    game_intro("Poker (Texas Hold'em)")
    press_enter_to_continue()

    deck = Deck()
    deck.shuffle()

    human = PokerPlayer(player.name, player.balance)
    cpu = PokerPlayer("CPU")

    human.deal_hole_cards([deck.deal_card(), deck.deal_card()])
    cpu.deal_hole_cards([deck.deal_card(), deck.deal_card()])

    clear_screen()
    dash_21()
    print(f"Your hand: {human.show_hand()}")
    print(f"CPU hand:  {cpu.show_hand(hide=True)}")
    dash_21()
    press_enter_to_continue()

    community_cards = []
    for i in range(3):
        community_cards = next_round(deck, community_cards, flop=(i == 0))


def next_round(deck, community_cards, flop=False):
    clear_screen()
    deck.deal_card()  # Burn a card

    if flop:
        community_cards = [deck.deal_card() for _ in range(3)]
    else:
        community_cards.append(deck.deal_card())

    dash_21()
    print(f"Community cards: {' '.join(str(card) for card in community_cards)}")
    dash_21()
    press_enter_to_continue()

    return community_cards
