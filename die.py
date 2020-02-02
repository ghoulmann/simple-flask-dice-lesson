from random import randint
class Die(object):
    def __init__(self, size):
        self.roll = str(randint(1, size))
