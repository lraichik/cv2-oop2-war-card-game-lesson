''' 
We are creating a deck of cards here for game of war
'''


from random import shuffle

cards = list(range(1,14))


class Deck():


    def __init__(self):
        self.cards = cards * 4 
        shuffle(self.cards) 


# Use this to test your code
# this is suuuper standard
if __name__ == "__main__":
    mydeck = Deck()
    print('Created deck object, shuffling cards')
    print('Here is your deck')
    print(mydeck.cards)

    print(mydeck.cards[0::2])
    print(mydeck.cards[1::2])
