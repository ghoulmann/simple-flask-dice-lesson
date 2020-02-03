from random import randint, choice
from datetime import datetime
class Die(object):
    def __init__(self, size):
        self.size = size
        self.timestamp = datetime.now()
        self.result = self.roll(self.size)
    def roll(self, size):
        size = int(size)
        if size % 2 == 0:
            if size == 2:
                return choice(['heads', 'tails']) 
            return str(randint(1, size))
        else:
            raise ValueError


