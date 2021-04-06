from bowling.logic.pin_set import PinSet


class Frame:
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
        if self.remaining_rolls > 0:
            self.remaining_rolls -= 1
            self.current_pin_set.roll(pins_hit)
            self.set_current_pin_set()

    def set_current_pin_set(self):
        if self.needs_new_pin_set() and self.can_add_pin_set():
            self.add_pin_set()
            if self.increment_rolls:
                self.increment_rolls = False
                self.remaining_rolls += 1

    def needs_new_pin_set(self):
        return self.current_pin_set.get_status() in ['Spare', 'Strike']

    def can_add_pin_set(self):
        return len(self.pin_sets) < self.max_pin_sets and \
               (self.remaining_rolls > 0 or self.increment_rolls)

    def add_pin_set(self):
        self.current_pin_set = PinSet()
        self.pin_sets.append(self.current_pin_set)

    def is_complete(self):
        if self.remaining_rolls == 0 or \
                self.needs_new_pin_set() and not self.can_add_pin_set():
            return True
        return False


