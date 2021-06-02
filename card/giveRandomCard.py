from random import choice

def card():

    cards = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
    return choice(cards)

def hand(number):
    cards = []

    for n in range(number):
        cards.append(card())

    return cards

# -- main --

n = int(input("Combien? "))
print(hand(n))