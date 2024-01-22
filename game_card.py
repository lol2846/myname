from random import shuffle

class Card:
    suits = ["pikey",'cherv', 'bubey','tref']
    values = [None,None,'2','3','4','5','6','7','8','9','10','valet','dame','king','tuz']
    def __init__(self,v,s):
        """suit and value - the numbers """
        self.v = v
        self.s = s
    def __It__(self,c2):
        if self.v < c2.v:
            return True
        if self.v == c2.v:
            if self.s < c2.s:
                return True
            else:
                return False
    def __gt__(self,c2):
        if self.v > c2.v:
            return True
        if self.v == c2.v:
            if self.s > c2.s:
                return True
            else:
                return False

    def __repr__(self):
        v = self.values[self.v] + " of " + self.suits[self.s]
        return v
    
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
    
class Player:
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("name of first palyer:")
        name2 = input("name of second player:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    def wins(self,winner):
        w = "{} take cards"
        w = w.format(winner)
        print(w)
    def draw(self,p1n, p1c, p2n, p2c):
        d = "{} put {}, and {} put {}"
        d = d.format(p1n, p1c,p2n,p2c)
        print(d)
    def play_game(self):
        cards = self.deck.cards
        print("Let's go")
        while len(cards) >= 2:
            m = "click X to exit. Click smth to enter the game"
            response = input(m)
            if response == 'X':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins+=1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("Game is over.{} winner".format(win))
    def winner(self, p1 , p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "nobody wins"
    
game = Game()
game.play_game()
