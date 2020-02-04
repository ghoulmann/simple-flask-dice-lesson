from dice import Dice

class Attribute(object):
    def __init__(self):
        self.tag = "attribute"
        a = Dice(6, 4, 1)
        self.result = a.attributes['attribute 1']