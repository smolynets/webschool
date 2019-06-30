from django.shortcuts import render

from .models import Video


def MainView(request):
    videos = Video.objects.all()
    if not request.user.is_authenticated:
        return render(request, 'landing_page.html', {})
    return render(request, 'home.html', {"videos": videos})


def VideoDetailView(request, pk):
    video = Video.objects.get(pk=pk)
    return render(request, 'video_detail.html', {"video": video})
