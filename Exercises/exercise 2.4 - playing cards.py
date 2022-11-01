import random

suits = ('clubs', 'diamonds', 'hearts', 'spades')
# or
# suits = 'clubs diamonds hearts spades'.split()
# or
# suits = ('♣', '♢', '♡', '♠')

ranks = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()

# cards = [f'{rank} of {suit}' for rank in ranks for suit in suits]
# or
cards = ['%s of %s' % (rank, suit) for rank in ranks for suit in suits]

random.shuffle(cards)

hand = [cards.pop() for _ in range(5)]
# or
# hand = sorted((cards.pop() for _ in range(5)), key = lambda c: suits.index(c.split()[-1]))

print(hand)