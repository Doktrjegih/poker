import random


class Card():
    def __init__(self):
        self.t = random.randint(2, 15)
        self.suit = random.choice(suit)

    def ne_init(self):
        return self.t, self.suit


def combo(cards):
    counter = 1
    for i in range(len(cards) - 1):
        if cards[i][0] == cards[i + 1][0]:
            counter += 1
    if counter == 2:
        print('пара')
    elif counter == 3:
        print('тройка')
    elif counter == 4:
        print('каре')


suit = ['spades', 'hearts', 'diamonds', 'clubs']
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
# all = [2, 2, 2, 2, 3, 4, 5]  # для тестов
print('все карты', all)
choise = input('откладываем\n')
arr_choise = []
for i in choise:
    arr_choise.append(all[int(i) - 1])
print(arr_choise)
combo(arr_choise)
