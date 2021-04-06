class PinSet:
    def __init__(self):
        self.max_rolls = 2
        self.rolls = []

    def roll(self, roll):
        if len(self.rolls) != self.max_rolls:
            self.rolls.append(roll)
