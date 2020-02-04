from die import Die

class Dice(object):
    def __init__(self, size, count, rounds):
        self.size = size
        self.count = count
        self.rounds = rounds
        self.rolls = {}
        for i in range(1, self.rounds + 1):
            self.rolls[i] = []
        for k in self.rolls.keys():
            for i in range(0, count):
                a = Die(self.size)
                self.rolls[k].append(int(a.result))
            self.rolls[k].sort()
            del self.rolls[k][0]
        self.attributes = self.getScores()
    def getScores(self):
        attributes = {}
        for i in range(1, self.rounds+1):
            attributes['Attribute ' + str(i)] = sum(self.rolls[i])
        return attributes
