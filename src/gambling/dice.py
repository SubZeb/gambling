from random import randint


class Dice(object):
    def __init__(self, num=1, sides=6):
        self.num = num
        self.sides = sides
        self.values = []
        for _ in range(self.num):
            self.values.append(randint(1,self.sides))
        self.roll()

    def roll(self):
        for i in range(self.num):
            self.values[i] = randint(1, self.sides)
