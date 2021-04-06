class Frame:
    def __init__(self, name):
        if name == 10:
            self.max_pin_sets = 3
        else:
            self.max_pin_sets = 1
        self.pin_sets = []
        self.score = 0
        self.name = name
