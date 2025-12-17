from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Video
from .forms import VideoUploadForm
from apps.comments.models import Comment

# Home page: recommended videos + search bar
def video_list(request):
    videos = Video.objects.filter(is_public=True).select_related('uploader')
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        videos = videos.filter(title__icontains=query)
    
    # Pagination
    paginator = Paginator(videos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'query': query
    }
    return render(request, 'videos/home.html', context)  # Use home.html as homepage
# Watch a single video page
def watch_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    
    # Increment views
    video.increment_views()
    
    # Get related videos
    related_videos = Video.objects.filter(
        is_public=True
    ).exclude(id=video.id).select_related('uploader')[:6]
    
    # Check if user liked this video
    user_liked = False
    if request.user.is_authenticated:
        user_liked = video.likes.filter(user=request.user).exists()
    
    # Fetch comments with related user and replies
    comments = Comment.objects.filter(video=video, parent=None).select_related('user').prefetch_related('replies')

    context = {
        'video': video,
        'related_videos': related_videos,
        'user_liked': user_liked,
        'comments': comments
    }
    return render(request, 'videos/watch.html',context )

# Upload a video
@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploader = request.user
            video.save()
            messages.success(request, 'Video uploaded successfully!')
            return redirect('videos:watch', video_id=video.id)  # Namespaced URL
    else:
        form = VideoUploadForm()
    
    return render(request, 'videos/upload.html', {'form': form}) 

# User's uploaded videos
@login_required
def my_videos(request):
    videos = Video.objects.filter(uploader=request.user)
    paginator = Paginator(videos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'videos/my_videos.html', {'page_obj': page_obj})

# Delete a video
@login_required
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id, uploader=request.user)
    if request.method == 'POST':
        video.delete()
        messages.success(request, 'Video deleted successfully!')
        return redirect('videos:my_videos')
    return render(request, 'videos/delete_confirm.html', {'video': video})


def watch_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)

    comments = Comment.objects.filter(
        video=video,
        parent=None
    ).select_related('user').prefetch_related('replies__user')

    return render(request, 'videos/watch.html', {
        'video': video,
        'comments': comments,
    })
def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'videos/video_detail.html', {'video': video})