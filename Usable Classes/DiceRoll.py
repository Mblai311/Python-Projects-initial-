import random


def dice_roll():
    result = random.randint(1, 6)
    return f"Your dice roll is {result}"


dice_roll()
