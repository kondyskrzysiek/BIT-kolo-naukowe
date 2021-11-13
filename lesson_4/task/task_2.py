from collections import Counter

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.value} of {self.suit}'

    def __hash__(self):
        return hash((self.suit,self.value))

class CardHand:
    def __init__(self):
        self.hand = Counter()

    def put_card(self,card):
        self.hand[card] += 1

    def get_card(self,card):
        if card in self.hand:
            self.hand[card] -=1
            return self.hand
        else:
            raise ValueError(
                f"No cards of type \"{card}\" left in hand!"
            )
    def __contains__(self,card):
        return card in self.hand

    def __len__(self,card):
        return sum(self.hand.values())

    def __str__(self):
        if not self.hand:
            return 'Card hand is empty'

        cards = [str(card) for card in self.hand.keys()]
        cards_str = "\n- ".join(cards)
        return f"Card hand:\n- {cards_str}"

class a:
    pass


if __name__ == '__main__':
    c = Card("ds","dsa")
    aw = a()
    print(c)