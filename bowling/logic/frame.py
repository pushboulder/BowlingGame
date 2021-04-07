from bowling.logic.pin_set import PinSet


class Frame:
    """ Controls a Bowling Frame using PinSet

    Instance variables:
        - name: Taken from init
        - max_pin_sets: `1` if `name` != 10 else `3`
        - increment_rolls: `False` if `name` != 10 else `True`
        - score: `int` 0
        - current_pin_set: `PinSet` Initialized
        - pin_sets: `list[PinSet]` contains `current_pin_set`
        - remaing_rolls: `int` 2

    """
    def __init__(self, name):
        if name == 10:
            self.max_pin_sets = 3
            self.increment_rolls = True
        else:
            self.max_pin_sets = 1
            self.increment_rolls = False
        self.score = 0
        self.name = name
        self.current_pin_set = PinSet()
        self.pin_sets = [self.current_pin_set]
        self.remaining_rolls = 2

    def roll(self, pins_hit):
        """ Sends a roll to PinSet

        :param pins_hit: The number of pins struck
        :type pins_hit: int
        """
        if self.remaining_rolls > 0:
            self.remaining_rolls -= 1
            self.current_pin_set.roll(pins_hit)
            self.set_current_pin_set()

    def set_current_pin_set(self):
        """ Sets the current_pin_set, only happens
            if another pin_set can be added
        """
        if self.needs_new_pin_set() and self.can_add_pin_set():
            self.add_pin_set()
            if self.increment_rolls:
                self.increment_rolls = False
                self.remaining_rolls += 1

    def needs_new_pin_set(self):
        """ Checks to see if our pin_set is complete and we need a new one.

        :return: True if current_pin_set status is 'Spare' or 'Strike'
        :rtype: bool
        """
        return self.current_pin_set.get_status() in ['Spare', 'Strike']

    def can_add_pin_set(self):
        """ Checks to see if a new pin_set can be added.

        :return: True if pin_sets length has reached max and one of
            the following is also True: remaining_rolls > 0 OR
            increment_rolls is True
        :rtype: bool
        """
        return len(self.pin_sets) < self.max_pin_sets and \
            (self.remaining_rolls > 0 or self.increment_rolls)

    def add_pin_set(self):
        """ Sets current_pin_set to a new PinSet and
            adds it to pin_sets.
        """
        self.current_pin_set = PinSet()
        self.pin_sets.append(self.current_pin_set)

    def is_complete(self):
        """ Checks to see if this Frame is complete

        :return: True if remaining_rolls is 0 or
            if a new pin is needed but can't be added
        :rtype: bool
        """
        if self.remaining_rolls == 0 or \
                self.needs_new_pin_set() and not self.can_add_pin_set():
            return True
        return False

    def calculate_score(self, future_rolls):
        """ Determines scores of all pin_sets and if rolls from later Frames are needed

        :param future_rolls: A list of rolls that were made after this Frame
        :type future_rolls: list[int]
        :return: The score for the Frame.
        :rtype: int
        """
        score = 0
        if self.is_complete():
            bonus_rolls = self.get_bonus_rolls_needed()
            if len(future_rolls) >= bonus_rolls:
                all_rolls = future_rolls[0:bonus_rolls]
                for pin_set in self.pin_sets:
                    all_rolls.extend(pin_set.rolls)
                score = sum(all_rolls)
        self.score = score
        return score

    def get_bonus_rolls_needed(self):
        """ Gets the amount of bonus rolls need based on frame.name or pin_set result

        :return: The number of rolls to obtain from future rolls
        :rtype: int
        """
        if self.name == 10:
            return 0
        if self.pin_sets[0].get_status() == 'Strike':
            return 2
        if self.pin_sets[0].get_status() == 'Spare':
            return 1
        return 0

