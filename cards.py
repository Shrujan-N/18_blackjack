import random

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["C", "D", "H", "S"]

class Deck:
    def __init__(self):
        self.reset()

    def reset(self):
        """Creates a full 52-card deck and shuffles it."""
        self.cards = [(rank, suit) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def draw(self):
        """Draws a card. Auto-replenishes and reshuffles if deck is empty."""
        if not self.cards:
            print("\n[Deck empty! Reshuffling new deck...]")
            self.reset()
        return self.cards.pop()

def hand_value(hand):
    """
    Calculates total score for a hand.
    Aces count as 11 unless total exceeds 21, in which case they drop to 1.
    """
    value = 0
    aces = 0

    for card in hand:
        rank = card[0]
        if rank == "A":
            aces += 1
            value += 11
        elif rank in {"J", "Q", "K"}:
            value += 10
        else:
            value += int(rank)

    # Reduce Ace from 11 to 1 dynamically if busting
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value