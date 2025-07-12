import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit 
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    
class Deck:
    def __init__(self):
        self.deck = []
        self.build_deck()

    def build_deck(self):
        suits = ["♥", "♦", "♣", "♠"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "J", "Q", "K", "A"]
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        total = 0
        ace_count = 0

        for card in self.hand:
            if card.rank.isdigit():
                total += int(card.rank)
            elif card.rank in ["J", "Q", "K"]:
                total += 10
            elif card.rank == "A":
                total += 11
                ace_count += 1

        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1

        return total
    
    def show_hand(self):
        return ' '.join(str(card) for card in self.hand)
    

p = Player("Test")
p.add_card(Card("A", "♠"))
p.add_card(Card("K", "♦"))
print(p.get_hand_value())  # Should print 21


