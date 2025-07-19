import time
from utils import clear_screen, dash_21, game_intro, press_enter_to_continue
from cards import Deck
from player import Player


# Player class for Poker
class PokerPlayer(Player):
    def __init__(self, name, balance=100, is_human=False):
        super().__init__(name, balance)
        self.hole_cards = []
        self.in_hand = True
        self.is_dealer = False
        self.is_human = is_human

    def deal_hole_cards(self, cards):
        self.hole_cards = cards

    def show_hand(self, hide=False):
        return "?? ??" if hide else ' '.join(str(card) for card in self.hole_cards)


def play_poker(player):
    game_intro("Poker (Texas Hold'em)")
    press_enter_to_continue()

    # Setup
    deck = Deck()
    deck.shuffle()
    small_blind = 10
    big_blind = 20

    human = PokerPlayer(player.name, player.balance, is_human=True)
    cpu = PokerPlayer("CPU", is_human=False)
    players = [human, cpu]

    # Rotate dealer
    if not hasattr(play_poker, "dealer_index"):
        play_poker.dealer_index = 0
    for i, p in enumerate(players):
        p.is_dealer = (i == play_poker.dealer_index)

    dealer = players[play_poker.dealer_index]
    sb = dealer
    bb = players[(play_poker.dealer_index + 1) % len(players)]

    # Post blinds
    pot = small_blind + big_blind
    sb.adjust_balance(-small_blind)
    bb.adjust_balance(-big_blind)

    # Set player bets
    for p in players:
        p.current_bet = 0
    sb.current_bet = small_blind
    bb.current_bet = big_blind
    current_bet = big_blind

    # Blinds summary
    clear_screen()
    dash_21()
    print(f"{dealer.name} is the dealer")
    print(f"{sb.name} posts small blind of ${small_blind}")
    print(f"{bb.name} posts big blind of ${big_blind}")
    dash_21()
    press_enter_to_continue()

    # Deal hole cards
    for p in players:
        p.deal_hole_cards([deck.deal_card(), deck.deal_card()])

    clear_screen()
    dash_21()
    print("Dealing hole cards...")
    time.sleep(2)
    for p in players:
        print(f"{p.name}'s hand: {p.show_hand(hide=not p.is_human)}")
    dash_21()
    press_enter_to_continue()

    # First betting round
    starting_index = (players.index(bb) + 1) % len(players)
    pot = run_betting_round(players, pot, current_bet, starting_index)

    # Community cards (Flop, Turn, River)
    community_cards = []
    for i in range(3):
        community_cards = next_round(deck, community_cards, flop=(i == 0))

    # Rotate dealer for next round
    play_poker.dealer_index = (play_poker.dealer_index + 1) % len(players)


def next_round(deck, community_cards, flop=False):
    clear_screen()
    deck.deal_card()  # Burn one card

    # Deal either 3 (flop) or 1 (turn/river) card
    if flop:
        community_cards = [deck.deal_card() for _ in range(3)]
    else:
        community_cards.append(deck.deal_card())

    dash_21()
    print(f"Community cards: {' '.join(str(card) for card in community_cards)}")
    dash_21()
    press_enter_to_continue()

    return community_cards


def get_betting_order(players, starting_index):
    # Rotate betting order starting at the correct index
    return players[starting_index:] + players[:starting_index]


def show_player_turn(p, pot, current_bet):
    """Unified turn display for human and CPU players"""
    clear_screen()
    dash_21()
    print(f"{p.name}'s turn")
    print(f"Hand: {p.show_hand(hide=not p.is_human)}")
    print(f"Pot: ${pot}")
    print(f"Current bet: ${current_bet}")
    print(f"{p.name}'s current bet: ${p.current_bet}")
    print(f"{p.name}'s balance: ${p.balance}")
    dash_21()
    time.sleep(1)


def run_betting_round(players, pot, current_bet, starting_index):
    betting_order = get_betting_order(players, starting_index)

    for p in betting_order:
        if not p.in_hand:
            continue

        # Shared turn display
        show_player_turn(p, pot, current_bet)

        if not p.is_human:
            # Auto-call for now
            call_amount = current_bet - p.current_bet
            p.adjust_balance(-call_amount)
            p.current_bet += call_amount
            pot += call_amount
            print(f"{p.name} calls ${call_amount}")
            time.sleep(2)
        else:
            # Human decision
            action = input("Call or fold? ").strip().lower()
            if action == "fold":
                p.in_hand = False
                print(f"{p.name} folds.")
                return pot
            elif action == "call":
                call_amount = current_bet - p.current_bet
                p.adjust_balance(-call_amount)
                p.current_bet += call_amount
                pot += call_amount
                print(f"{p.name} calls ${call_amount}")
                time.sleep(1)
            else:
                print("Invalid input. Treated as fold.")
                p.in_hand = False
                return pot

    return pot




