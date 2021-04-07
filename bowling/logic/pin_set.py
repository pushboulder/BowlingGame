class PinSet:
    """ Controls a set a 10 pins and limits rolls to 2

    Instance variables:
        - max_rolls - int default: 2
        - rolls - list default: []
    """
    def __init__(self):
        self.max_rolls = 2
        self.rolls = []

    def roll(self, pins_hit):
        """ Adds value to rolls list if possible

        :param pins_hit: The number of pins struck
        :type pins_hit: int
        """
        if len(self.rolls) != self.max_rolls:
            self.rolls.append(pins_hit)

    def get_status(self):
        """ Returns the result of the pin set

        :return: Strike, Spare, Incomplete or Complete
        :rtype: str
        """
        max_reached = len(self.rolls) == self.max_rolls
        if sum(self.rolls) == 10:
            if max_reached:
                return 'Spare'
            return 'Strike'
        if max_reached:
            return 'Complete'
        return 'Incomplete'


