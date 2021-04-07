from bowling.logic.game_style import GameStyle


def get_template(game_id):
    template = 'game.html'
    if game_id is None:
        template = 'base.html'
    return template


def get_context(game_id, pins_hit):
    context = {}
    if game_id is not None:
        context = get_game_context(game_id, pins_hit)
    return context


def get_game_context(game_id, pins_hit):
    game_style = GameStyle(get_clean_id(game_id))
    if pins_hit:
        game_style.roll(get_clean_pins(pins_hit))
    return game_style.get_context()


def get_clean_id(game_id):
    return None if game_id == 'create' else game_id


def get_clean_pins(pins_hit):
    return int(pins_hit)
