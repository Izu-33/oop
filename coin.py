import random


class Coin:

    def __init__(self):
        self.sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup


kobo = Coin()
penny = Coin()
cents = Coin()

print("Before Tossing:")
print(kobo.get_sideup())
print(penny.get_sideup())
print(cents.get_sideup())

kobo.toss()
penny.toss()

print()
print("After Tossing:")
print(kobo.get_sideup())
print(penny.get_sideup())
print(cents.get_sideup())