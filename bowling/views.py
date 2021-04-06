from django.shortcuts import render


def game_view(request, game_id=None):
    game_id = request.POST.get('game_id', game_id)
    return render(
        request=request,
        context={'game_id': game_id},
        template_name='base.html'
    )
