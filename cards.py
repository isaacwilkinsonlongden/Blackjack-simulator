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