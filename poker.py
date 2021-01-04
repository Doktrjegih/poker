import random


class Card():
    def __init__(self):
        self.t = random.randint(2, 15)

    def ne_init(self):
        return self.t

table = []
for i in range(5):
    a = Card()
    c = a.ne_init()
    table.append(c)
print('стол', table)
hand = []
for i in range(2):
    a = Card()
    c = a.ne_init()
    hand.append(c)
print('рука', hand)
all = table + hand
print('все карты', all)
choise = input('откладываем')
arr_choise = []
for i in choise:
    arr_choise.append(all[int(i) - 1])
print(arr_choise)
