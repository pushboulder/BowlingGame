class PinSet:
    def __init__(self):
        self.max_rolls = 2
        self.rolls = []

    def roll(self, pins_hit):
        if len(self.rolls) != self.max_rolls:
            self.rolls.append(pins_hit)

    def get_status(self):
        max_reached = len(self.rolls) == self.max_rolls
        if sum(self.rolls) == 10:
            if max_reached:
                return 'Spare'
            return 'Strike'
        if max_reached:
            return 'Complete'
        return 'Incomplete'


