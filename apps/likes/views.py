from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Like
from apps.videos.models import Video

@login_required
@require_POST
def toggle_like(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    
    like, created = Like.objects.get_or_create(
        video=video,
        user=request.user
    )
    
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    
    likes_count = video.get_likes_count()
    
    return JsonResponse({
        'success': True,
        'liked': liked,
        'likes_count': likes_count
    })

@login_required
def liked_videos(request):
    likes = Like.objects.filter(user=request.user).select_related('video__uploader')
    videos = [like.video for like in likes]
    
    from django.core.paginator import Paginator
    paginator = Paginator(videos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'likes/liked_videos.html', {'page_obj': page_obj})