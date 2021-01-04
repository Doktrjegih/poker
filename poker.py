import random

class Card():
    def __init__(self):
        self.t = random.randint(2, 15)
    
    def array(self):
        a = []
        for i in range(5):
            a.append(self.t)
        return a

b = Card()
print(b.array())