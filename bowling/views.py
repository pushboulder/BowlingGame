from django.shortcuts import render
from bowling.logic.game_style import GameStyle


def game_view(request, game_id=None):
    game_id = request.POST.get('game_id', game_id)
    context = {}
    template = 'base.html'
    if game_id is not None:
        template = 'game.html'
        if game_id == 'create':
            game_id = None
        game_style = GameStyle(game_id)
        pins_hit = request.POST.get('pins_hit', None)
        if pins_hit is not None:
            game_style.roll(int(pins_hit))
        context = game_style.get_context()
    return render(
        request=request,
        context=context,
        template_name=template
    )
