#!/usr/bin/python
from random import shuffle

suites = "D S H C".split()
cardVals = "A K Q J 10 9 8 7 6 5 4 3 2".split()

class Deck:
    """docstring for Deck."""
    def __init__(self,suites,cardVals):
        self.suites = suites
        self.cardVals = cardVals
        self.cardDeckSize = 52
        self.full = True
        self.deck = []
    def makeDeck(self):
        for i in range(0,len(self.suites)):
            for j in range(0,len(self.cardVals)):
                self.deck.append(self.cardVals[j]+self.suites[i])
    def split(self):
        if len(self.deck) < 52:
            print("shuffle deck first")
        else:
            print("splitting")
    def shuffleD(self):
        shuffle(self.deck)
        return self.deck[:26],self.deck[26:]



class Hand():
    """docstring for Hand."""
    def __init__(self,halfDeck):
        self.hand = halfDeck
        self.handSize = len(self.hand)
    def addCard(self,card):
        self.hand.append(card)
        self.handSize += 1
    def removeCard(self):
        if self.handSize >= 1:
            self.handSize -= 1
            return self.hand.pop(0)
        else:
            print("No more cards")
class Player(Hand):
    """docstring for Player."""
    def __init__(self,name,halfDeck):
        self.name = name
        Hand.__init__(self,halfDeck)

def faceToVal(faceVal):
    if faceVal == 'A':
        return 14
    elif faceVal == 'K':
        return 13
    elif faceVal == 'Q':
        return 12
    elif faceVal == 'J':
        return 11

def removeThree(player):
    warSet = []
    for i in range(0,2):
        warSet.append(player.removeCard())
    return warSet

def checkThreeWinner(setOne, setTwo):
    for i in range(0,2):
        if(setOne[i] > setTwo[i]):
            return 1
        if(setOne[i] <= setTwo[i]):
            return 2

if __name__ == '__main__':
    gameDeck = Deck(suites, cardVals)
    gameDeck.makeDeck()
    h1, h2 = gameDeck.shuffleD()
    playerOne = Player("g",h1)
    playerTwo = Player("t",h2)
    #gameDeck.split()
    #print(gameDeck.deck)
    print(playerOne.hand)
    print(playerTwo.hand)
    c1 = playerOne.removeCard()
    c2 = playerTwo.removeCard()
    print(c1[0])
    print(c2[0])
    if c1[0].isalpha():
        print("face")
    if c2[0].isalpha():
        print("face")


    while(playerOne.handSize > 0 or playerTwo.handSize > 0)
    {
        card1 = playerOne.removeCard()
        card2 = playerTwo.removeCard()
        p1Set = []
        p1Sest = []
        #check if face card and convert

        #determine winner and add cards to winner.hand OR

        #for tie, remove three cards from each hand determine if face and
        #find winner

    }
