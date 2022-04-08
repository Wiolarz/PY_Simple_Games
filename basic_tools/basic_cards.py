import random

class Card:
    def __init__(self, color, value):
        self.value = value
        self.color = color

    def str_color(self):
        color_symbols = ["♠", "♥", "♦", "♣"]
        return color_symbols[self.color]

    def str_value(self):
        value_symbols = ["J", "Q", "K", "A"]
        if self.value > 10:
            return value_symbols[self.value - 11]
        else:
            return str(self.value)

    def __repr__(self):
        return self.str_color() + " " + self.str_value()

class Deck_manager:
    def __init__(self):
        self.deck = []
        self.used_cards = []  # discarded cards, may be used to reshuffle the deck

        self.generate_cards()

    def generate_cards(self):
        self.deck = []
        for color in range(4):
            for value in range(2, 15):
                self.deck.append(Card(color, value))
        self.shuffle()

    def reset_deck(self):
        self.deck = self.used_cards
        self.shuffle()
        self.used_cards = []

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self, value=None):
        if value == None:
            value = 1
        stack = []
        try:
            x = value - len(self.deck)
        except:
            print("error")
        if x > 0:
            for i in self.deck:
                stack.append(i)

            self.reset_deck()
            if x > len(self.deck):
                print("error: game logic: too many cards in use")
                exit(2)
            for i in range(x):
                stack.append(self.deck[-1])
                self.deck.pop()
        else:
            for i in range(value):
                stack.append(self.deck[-1])
                self.deck.pop()
        return stack

class Player:
    def __init__(self, deck):
        self.deck_in_use = deck
        self.hand = []


    def use_card(self, choice=None):
        if choice == None:
            choice = 0
        elif choice >= len(self.hand):
            choice = len(self.hand) - 1

        if len(self.hand) == 0:
            print("player has no cards left to use")
            return

        chosen_card = self.hand[choice]
        self.deck_in_use.used_cards.append(chosen_card)
        self.hand.pop(choice)
        return chosen_card

    def draw(self, value=1):
        stack = self.deck_in_use.draw(value)
        for card in stack:
            self.hand.append(card)

if __name__ == '__main__':
    deck = Deck_manager()

    p1 = Player(deck)
    p2 = Player(deck)
    p3 = Player(deck)
    p4 = Player(deck)

    p1.draw(20)
    p2.draw(15)
    for i in range(15):
        #pass
        p1.use_card()
    p3.draw(15)
    p4.draw(15)