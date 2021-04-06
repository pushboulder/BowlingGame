class PinSet:
    max_rolls = 2
    rolls = []

    def roll(self, roll):
        if len(self.rolls) != self.max_rolls:
            self.rolls.append(roll)
