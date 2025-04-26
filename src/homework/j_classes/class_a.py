import random

class Die:
    __roll_value = None

    def roll(self):
        Die.__roll_value = random.randint(1, 6)

    def get_rolled_value(self):
        return Die.__roll_value
    
    def __str__(self):
        return f"The rolled value is {Die.__roll_value}"