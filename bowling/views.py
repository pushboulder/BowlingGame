from django.shortcuts import render
from bowling.logic.views import get_context, get_template


def game_view(request, game_id=None):
    game_id = request.POST.get('game_id', game_id)
    pins_hit = request.POST.get('pins_hit', None)
    context = get_context(game_id, pins_hit)
    template = get_template(game_id)
    return render(
        request=request,
        context=context,
        template_name=template
    )


