# Create your views here.
from django.shortcuts import render
from .models import Video


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videos/video_list.html', {'videos': videos})


def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'videos/video_detail.html', {'video': video})
