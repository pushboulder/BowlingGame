from bowling.logic.pin_set import PinSet


class Frame:
    def __init__(self, name):
        if name == 10:
            self.max_pin_sets = 3
        else:
            self.max_pin_sets = 1
        self.pin_sets = []
        self.score = 0
        self.name = name
        self.current_pin_set = None

    def roll(self, pins_hit):
        self.set_current_pin_set()
        self.current_pin_set.roll(pins_hit)

    def set_current_pin_set(self):
        if self.needs_new_pin_set() and self.can_add_pin_set():
            self.add_pin_set()

    def needs_new_pin_set(self):
        return self.current_pin_set is None or self.current_pin_set.get_status() != 'Incomplete'

    def can_add_pin_set(self):
        return len(self.pin_sets) < self.max_pin_sets

    def add_pin_set(self):
        self.current_pin_set = PinSet()
        self.pin_sets.append(self.current_pin_set)


