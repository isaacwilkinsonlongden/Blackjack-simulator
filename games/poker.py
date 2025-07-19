import time
from utils import clear_screen, dash_21, game_intro, press_enter_to_continue
from cards import Deck
from player import Player


class PokerPlayer(Player):
    def __init__(self, name, balance=100):
        super().__init__(name, balance)
        self.hole_cards = []
        self.in_hand = True
        self.is_dealer = False

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

    small_blind = 10
    big_blind = 20

    human = PokerPlayer(player.name, player.balance)
    cpu = PokerPlayer("CPU")
    players = [human, cpu]

    if not hasattr(play_poker, "dealer_index"):
        play_poker.dealer_index = 0

    for i, p in enumerate(players):
        p.is_dealer = (i == play_poker.dealer_index)

    dealer = players[play_poker.dealer_index]
    sb = dealer
    bb = players[(play_poker.dealer_index + 1) % len(players)]
    pot = 0
    sb.adjust_balance(-small_blind)
    bb.adjust_balance(-big_blind)
    pot += small_blind + big_blind

    clear_screen()
    dash_21()
    print(f"{dealer.name} is the dealer")
    print(f"{sb.name} posts small blind of ${small_blind}")
    print(f"{bb.name} posts big blind of ${big_blind}")
    print(f"Pot: ${pot}")
    dash_21()
    press_enter_to_continue()

    for p in players:
        p.deal_hole_cards([deck.deal_card(), deck.deal_card()])

    clear_screen()
    dash_21()
    print(f"Your hand: {human.show_hand()}")
    for p in players:
        if p != human:
            print(f"{p.name}'s hand: {p.show_hand(hide=True)}")
    dash_21()
    press_enter_to_continue()

    community_cards = []
    for i in range(3):
        community_cards = next_round(deck, community_cards, flop=(i == 0))

    play_poker.dealer_index = (play_poker.dealer_index + 1) % len(players)


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
