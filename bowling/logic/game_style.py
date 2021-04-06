from bowling.logic.game_manager import GameManager


class GameStyle:

    def __init__(self, game_id=None):
        self.game_manager = GameManager(game_id)

    @staticmethod
    def get_headers():
        headers = {}
        for index in range(1, 12):
            headers[index] = index
        headers[11] = 'Total Score'
        return headers

    def get_roll_results(self):
        roll_results = []
        for name, frame in self.game_manager.frames.items():
            frame_results = []
            for pin_set in frame.pin_sets:
                status = pin_set.get_status()
                frame_results.extend(self.get_strike_results(status, name))
                frame_results.extend(self.get_spare_results(status, pin_set))
                frame_results.extend(self.get_normal_results(status, pin_set))
            frame_results.extend(self.get_blank_results(name, len(frame_results)))
            roll_results.extend(frame_results)

        return roll_results

    @staticmethod
    def get_strike_results(status, name):
        strike_result = []
        if status == 'Strike':
            if name != 10:
                strike_result.append('')
            strike_result.append('X')
        return strike_result

    @classmethod
    def get_spare_results(cls, status, pin_set):
        spare_results = []
        if status == 'Spare':
            roll_1 = cls.convert_zero_result(pin_set.rolls[0])
            spare_results.extend([roll_1, '/'])
        return spare_results

    @staticmethod
    def convert_zero_result(roll):
        return str(roll) if roll != 0 else '-'

    @classmethod
    def get_normal_results(cls, status, pin_set):
        normal_results = []
        if status in ['Complete', 'Incomplete']:
            for roll in pin_set.rolls:
                normal_results.append(cls.convert_zero_result(roll))
        return normal_results

    @staticmethod
    def get_blank_results(name, count):
        blanks_list = []
        required_results = 3 if name == 10 else 2
        while count < required_results:
            blanks_list.append('')
            count += 1
        return blanks_list
