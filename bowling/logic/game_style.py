from bowling.logic.game_manager import GameManager


class GameStyle:
    """ Controls how to style a Game for template context

    Instance Variables:
        - game_manager - GameManager
    """
    def __init__(self, game_id=None):
        self.game_manager = GameManager(game_id)

    def roll(self, pins_hit):
        """ Sends 'pins_hit' through 'GameManager'

        :param pins_hit: The number of pins struck
        :type pins_hit: int
        """
        self.game_manager.roll(pins_hit)

    def get_context(self):
        """ Obtains a 'Game' context for templates

        :return: dict context for template
        :rtype: dict
        """
        context = {
            'game_id': self.game_manager.game.id,
            'active': self.game_manager.game.active,
            'headers': self.get_headers(),
            'rolls': self.get_roll_results(),
            'scores': self.get_scores()
        }
        context.update(
            self.get_current_frame_data()
        )
        return context

    def get_current_frame(self):
        """ Helper method to get the current 'Frame' of a 'Game'

        :return: The current Frame of the Game
        :rtype: bowling.logic.frame.Frame
        """
        return self.game_manager.frames[self.game_manager.game.current_frame]

    @staticmethod
    def get_headers():
        """ Obtains header information for templates

        :return: Dictionary with id as key and display as value
        :rtype: list[str,int]
        """
        headers = {}
        for index in range(1, 12):
            headers[index] = index
        headers[11] = 'Total Score'
        return headers

    def get_roll_results(self):
        """ Obtains a list of roll results for templates

        :return: list of results for the Game
        :rtype: list[str]
        """
        roll_results = []
        for name, frame in self.game_manager.frames.items():
            frame_results = self.get_frame_result(frame, name)
            roll_results.extend(frame_results)

        return roll_results

    def get_frame_result(self, frame, name):
        """ Obtains list of roll results by frame

        :param frame: Frame to extract data from
        :type frame: bowling.logic.frame.Frame
        :param name: The name of the Frame
        :type name: int
        :return: list of results for the Frame
        :rtype: list[str]
        """
        frame_results = []
        for pin_set in frame.pin_sets:
            self.get_pin_set_result(frame_results, name, pin_set)
        self.get_blank_results(frame_results, name, len(frame_results))
        return frame_results

    def get_pin_set_result(self, frame_results, name, pin_set):
        """ Updates frame_results with data from a 'PinSet'

        :param frame_results: list to update results to
        :type frame_results: list
        :param name: The name of the Frame
        :type name: int
        :param pin_set: The PinSet to extract roll results from
        :type pin_set: bowling.logic.pin_set.PinSet
        """
        status = pin_set.get_status()
        self.get_strike_results(frame_results, status, name)
        self.get_spare_results(frame_results, status, pin_set)
        self.get_normal_results(frame_results, status, pin_set)

    @staticmethod
    def get_strike_results(frame_results, status, name):
        """ Updates frame_results with data if status is 'Strike'

        :param frame_results: list to update results to
        :type frame_results: list
        :param status: The status of a 'PinSet'
        :type status: str
        :param name: The name of the Frame
        :type name: int
        """
        if status == 'Strike':
            if name != 10:
                frame_results.append('')
            frame_results.append('X')

    def get_spare_results(self, frame_results, status, pin_set):
        """ Updates frame_results with data if status is 'Spare'

        :param frame_results: list to update results to
        :type frame_results: list
        :param status: The status of a 'PinSet'
        :type status: str
        :param pin_set: The PinSet to extract roll results from
        :type pin_set: bowling.logic.pin_set.PinSet
        """
        if status == 'Spare':
            roll_1 = self.convert_zero_result(pin_set.rolls[0])
            frame_results.extend([roll_1, '/'])

    @staticmethod
    def convert_zero_result(roll):
        """ Converts 0 result to '-'

        :param roll: number representing number of pins hit
        :type roll: int
        :return: roll as str, possible changed to '-'
        :rtype: str
        """
        return str(roll) if roll != 0 else '-'

    def get_normal_results(self, frame_results, status, pin_set):
        """ Updates frame_results with results that don't have special bonuses

        :param frame_results: list to update results to
        :type frame_results: list
        :param status: The status of a 'PinSet'
        :type status: str
        :param pin_set: The PinSet to extract roll results from
        :type pin_set: bowling.logic.pin_set.PinSet
        """
        if status in ['Complete', 'Incomplete']:
            for roll in pin_set.rolls:
                frame_results.append(self.convert_zero_result(roll))

    @staticmethod
    def get_blank_results(frame_results, name, count):
        """ Updates frame_results with empty fields if it does not have enough

        :param frame_results: list to update results to
        :type frame_results: list
        :param name: The name of the Frame
        :type name: int
        :param count: The current total of results obtained
        :type count: int
        """
        required_results = 3 if name == 10 else 2
        while count < required_results:
            frame_results.append('')
            count += 1

    def get_scores(self):
        """ Obtains list of scores for templates

        :return: list of scores for each frame
        :rtype: list[str, int]
        """
        total_score = 0
        scores = []
        self.game_manager.calculate_score()
        for frame in self.game_manager.frames.values():
            total_score = self.get_frame_score(frame, scores, total_score)
        total_score = '' if '' in scores else total_score
        scores.append(total_score)
        return scores

    @staticmethod
    def get_frame_score(frame, scores, total_score):
        """ Updates total_score with the score of the frame

        :param frame: Frame to extract data from
        :type frame: bowling.logic.frame.Frame
        :param scores: list of scores to update
        :type scores: list
        :param total_score: the score to increment
        :type total_score: int
        :return: The total score
        :rtype: int
        """
        score = frame.score if frame.score != 0 else ''
        if score:
            total_score += score
            scores.append(total_score)
        else:
            scores.append('')
        return total_score

    def get_current_frame_data(self):
        """ Obtains context for data relevant to the current frame

        :return: Dictionary containing rolls_remaining,
            current_frame, available_pins
        :rtype: dict
        """
        rolls = self.get_current_frame().remaining_rolls
        rolls = 0 if not self.game_manager.game.active else rolls
        current_frame_data = {
            'rolls_remaining': rolls,
            'current_frame': self.game_manager.game.current_frame,
            'available_pins': self.get_available_pins()
        }
        return current_frame_data

    def get_available_pins(self):
        """ Obtains context data of available pins for templates

        :return: dictionary of 'id' with bool
        :rtype: dict
        """
        available_range = range(0, 11 - sum(self.get_current_frame().pin_sets[-1].rolls))
        if not self.game_manager.game.active:
            available_range = []
        available_pins = {}
        for index in range(0, 11):
            available_pins[index] = index in available_range

        return available_pins

