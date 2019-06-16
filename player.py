from deck import Deck

class Player():


    def __init__(self, 
                name = 'Adam', 
                win_slogan = 'Great game', 
                lose_slogan = 'Great game as well'):
        self.hand = []
        self.name = name
        self.win_slogan = win_slogan
        self.lose_slogan = lose_slogan

    def draw_one(self):
        top_card = self.hand[0]
        self.hand.pop(0)
        return top_card
        

    def take_winnings(self, cards):
        self.hand.extend(cards)
