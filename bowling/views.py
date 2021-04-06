from django.shortcuts import render


def game_view(request):
    return render(
        request=request,
        context={},
        template_name='base.html'
    )
