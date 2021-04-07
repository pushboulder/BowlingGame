from bowling.logic.game_style import GameStyle


def get_template(game_id):
    """ Obtains the template name to load based on `game_id`

    :param game_id: Identifier for Game Model
    :type game_id: int
    :return: The name of a template
    :rtype: str
    """
    template = 'game.html'
    if game_id is None:
        template = 'base.html'
    return template


def get_context(game_id, pins_hit):
    """ Obtains the context for a template based on game_id and pins_hit

    :param game_id: Identifier for Game Model
    :type game_id: int
    :param pins_hit: Number of pins hit, used to look up Roll Model
    :type pins_hit: int
    :return: Empty dict if no game_id is given
    :rtype: dict
    """
    context = {}
    if game_id is not None:
        context = get_game_context(game_id, pins_hit)
    return context


def get_game_context(game_id, pins_hit):
    """ Obtains the context from 'GameStyle' using game_id and pins_hit

    :param game_id: Identifier for Game Model
    :type game_id: int
    :param pins_hit: Number of pins hit, used to look up Roll Model
    :type pins_hit: int
    :return: dictionary containing context for displaying a game
    :rtype: dict
    """
    game_style = GameStyle(get_clean_id(game_id))
    if pins_hit:
        game_style.roll(get_clean_pins(pins_hit))
    return game_style.get_context()


def get_clean_id(game_id):
    """ Returns 'None' if the 'game_id' is create or just returns the 'game_id'

    :param game_id: Identifier for Game Model
    :type game_id: int
    :return: str/None
    :rtype: int
    """
    return None if game_id == 'create' else game_id


def get_clean_pins(pins_hit):
    """ Returns the given 'pins_hit' as 'int'

    :param pins_hit: Number of pins hit, used to look up Roll Model
    :type pins_hit: int/str
    :return: pins_hit converted to int
    :rtype: int
    """
    return int(pins_hit)
