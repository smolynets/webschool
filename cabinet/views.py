from django.shortcuts import render

from .models import Video


def main_view(request):
    videos = Video.objects.all()
    if not request.user.is_authenticated:
        return render(request, 'landing_page.html', {})
    return render(request, 'home.html', {"videos": videos})
