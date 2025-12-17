from django.shortcuts import render
from apps.videos.models import Video

def welcome_view(request):
    featured_videos = Video.objects.all()[:5]  # first 5 videos
    recommended_videos = Video.objects.order_by('-likes')[:5]  # top liked videos
    return render(request, 'welcome.html', {
        'featured_videos': featured_videos,
        'recommended_videos': recommended_videos,
    })


