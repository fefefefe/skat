# card game Skat

""" 
features so far:
hands out the cards
calculates the Jacks' factor

suit code is:
0 == diamonds
1 == hearts
2 == spades
3 == clubs

rank code is:
0 == 7
1 == 8
2 == 9
3 == 10
4 == Jack
5 == Queen
6 == King
7 == Ace
"""

import random

# variable declarations
hand0 = [] # the players hand
hand1 = [] # cpu1's hand
hand2 = [] # cpu2's hand
skat = [] # the 2 table cards

# build the deck of 32 cards and shuffle it
def makeDeck():
    deck = []
    for suit in range(0, 4):
        for rank in range(0, 8):
            deck.append([rank, suit])
    random.shuffle(deck)
    return deck

# give out the cards to each player
def giveCards(deck):
    global hand0
    global hand1
    global hand2
    global skat
    hand0 = deck[:3]
    hand1 = deck[3:6]
    hand2 = deck[6:9]
    skat = deck[9:11]
    hand0 += deck[11:15]
    hand1 += deck[15:19]
    hand2 += deck[19:23]
    hand0 += deck[23:26]
    hand1 += deck[26:29]
    hand2 += deck[29:]

# readable hand
def translateHand(hand):
        for e in hand:
            if e[0] == 0:
                e[0] = "7"
            elif e[0] == 1:
                e[0] = "8"
            elif e[0] == 2:
                e[0] = "9"
            elif e[0] == 3:
                e[0] = "10"
            elif e[0] == 4:
                e[0] = "Jack"
            elif e[0] == 5:
                e[0] = "Queen"
            elif e[0] == 6:
                e[0] = "King"
            elif e[0] == 7:
                e[0] = "Ace"
            if e[1] == 0:
                e[1] = "Diamonds"
            elif e[1] == 1:
                e[1] = "Hearts"
            elif e[1] == 2:
                e[1] = "Spades"
            elif e[1] == 3:
                e[1] = "Clubs"
        print hand

def calcFactor(hand):
    jacks = []
    for e in hand:
        if e[0] == "Jack":
            jacks += [e[1]]
    withOrWithout = ""
    factor = 0
    if "Clubs" in jacks:
        withOrWithout = "with"
        factor += 1
        if "Spades" in jacks:
            factor += 1
            if "Hearts" in jacks:
                factor += 1
                if "Diamonds" in jacks:
                    factor += 1
    else:
        withOrWithout = "without"
        factor += 1
        if "Spades" not in jacks:
            factor += 1
            if "Hearts" not in jacks:
                factor += 1
                if "Diamonds" not in jacks:
                    factor += 1
    print jacks
    print "The factor is:", withOrWithout, factor, "plays", factor + 1
    return factor
            
# set up one round
deck = makeDeck()
giveCards(deck)
# to do: sortHand(hand0)

# test: decode hands
print
print "--------------------------------------------"
print "              Show all hands                "
print "--------------------------------------------"
print
translateHand(hand0)
print
translateHand(hand1)
print
translateHand(hand2)
print
translateHand(skat)
print

# test: calculate Jacks' factor
print
print "--------------------------------------------"
print "     Calculate the Jacks' factors           "
print "--------------------------------------------"
print
print "Player has the following Jacks:"
calcFactor(hand0)
print
print "CPU1 has the following Jacks:"
calcFactor(hand1)
print
print "CPU2 has the following Jacks:"
calcFactor(hand2)




