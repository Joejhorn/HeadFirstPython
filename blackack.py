import random

suits = ["hearts", "diamonds", "clubs", "spades"]
faces = ["Jack", "Queen", "King", "Ace"]
numbered = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

def draw(deck):
    card = random.choice(list(deck))
    deck.remove(card)
    return card


if __name__ == "__main__":
    deck = set()
    for suit in suits:
        for card in faces + numbered:
            deck.add((card, " of ", suit))
    card = draw(deck)
    print(card)
    print(len(deck))

  

