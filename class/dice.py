import random
random_dice = random.randint
class Dice:
    def roll(self):
        return (random_dice(1,6), random_dice(1,6))
        

dice1 = Dice()
print(dice1.roll())