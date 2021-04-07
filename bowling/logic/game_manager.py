from bowling.models.game import Game
from bowling.models.game_roll import GameRoll
from bowling.models.roll import Roll
from bowling.logic.frame import Frame


class GameManager:
    """ Manages a Game Model through Frame objects.

    Instance variables:
        - game - Game takes game_id
        - frames - dict[int:Frame]
    """
    def __init__(self, game_id=None):
        self.game = self.get_game(game_id)
        self.frames = self.get_frames()
        game_rolls = self.get_game_rolls()
        self.load_frames(game_rolls)

    def get_game(self, game_id):
        """ Obtains a Game Model object by either loading or creating one.

        :param game_id: Game Model identifier
        :type game_id: int
        :return: Game Model object
        :rtype: bowling.models.game.Game
        """
        if game_id is None:
            return self.create_game()
        return self.load_game(game_id)

    @staticmethod
    def load_game(game_id):
        """ Loads a Game object with game_id

        :param game_id: Game Model identifier
        :type game_id: int
        :return: Game Model object
        :rtype: bowling.models.game.Game
        """
        return Game.objects.get(id=game_id)

    @staticmethod
    def create_game():
        """ Creates a Game object

        :return: Game Model object
        :rtype: bowling.models.game.Game
        """
        return Game.objects.create()

    @staticmethod
    def get_frames():
        """ Obtains a dict of Frames keys are Frame.name 1-10

        :return: dict of Frames, keys are Frame.name 1-10
        :rtype: dict[int, bowling.logic.frame.Frame]
        """
        frames = {}
        for index in range(1, 11):
            frames[index] = Frame(index)
        return frames

    def get_game_rolls(self):
        """ Obtains list of GameRoll objects for Game

        :return: list of GameRoll objects
        :rtype: list[bowling.models.game_roll.GameRoll]
        """
        game_rolls = []
        for game_roll in GameRoll.objects.filter(game__id=self.game.id):
            game_rolls.append(game_roll)
        return game_rolls

    def roll(self, pins_hit):
        """ Sends a roll to PinSet through Frame

        :param pins_hit: The number of pins struck
        :type pins_hit: int
        """
        if self.game.active:
            self.update_frame(pins_hit)
            self.add_game_roll(pins_hit)

    def calculate_score(self):
        """ Updates scores for all frames
        """
        current_roll = 0
        pins_hit_list = self.get_pins_hit_list()
        for frame in self.frames.values():
            current_roll += (2 - frame.remaining_rolls)
            frame.calculate_score(pins_hit_list[current_roll:current_roll + 2])

    def load_frames(self, game_rolls):
        """ Loads all frames with GameRolls for the Game

        :param game_rolls: list of GameRoll objects
        :type game_rolls: list[bowling.model.game_roll.GameRoll]
        """
        current_frame = 1
        for game_roll in game_rolls:
            self.frames[current_frame].roll(game_roll.roll.pins_hit)
            if self.frames[current_frame].is_complete() and current_frame != 10:
                current_frame += 1

    def update_frame(self, pins_hit):
        """ Updates the current Frame with a roll.
            If needed, increments Game.current_frame and Game.is_active

        :param pins_hit: The number of pins struck
        :type pins_hit: int
        """
        self.frames[self.game.current_frame].roll(pins_hit)
        if self.frames[self.game.current_frame].is_complete():
            if self.game.current_frame == 10:
                self.game.active = False
            else:
                self.game.current_frame += 1
            self.game.save()

    def get_pins_hit_list(self):
        """ Changes GameRolls to flat list of pins_hit values

        :return: list of pins struck
        :rtype: list[int]
        """
        pins_hit = GameRoll.objects.filter(game=self.game).values_list('roll__pins_hit', flat=True)
        return list(pins_hit)

    def add_game_roll(self, pins_hit):
        """ Creates a new GameRoll object attached to Game

        :param pins_hit: The number of pins struck
        :type pins_hit: int
        """
        GameRoll.objects.create(
            game=self.game,
            roll=Roll.objects.get(pins_hit=pins_hit)
        )


