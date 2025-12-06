from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Comment
from apps.videos.models import Video

@login_required
def add_comment(request, video_id):
    if request.method == 'POST':
        video = get_object_or_404(Video, id=video_id)
        text = request.POST.get('text')
        parent_id = request.POST.get('parent_id')
        
        if text:
            comment = Comment.objects.create(
                video=video,
                user=request.user,
                text=text,
                parent_id=parent_id if parent_id else None
            )
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'comment_id': comment.id,
                    'username': comment.user.username,
                    'text': comment.text,
                    'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
                })
            
            messages.success(request, 'Comment added successfully!')
        else:
            messages.error(request, 'Comment cannot be empty!')
    
    return redirect('videos:watch', video_id=video_id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    video_id = comment.video.id
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
    
    return redirect('videos:watch', video_id=video_id)

def get_comments(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    comments = Comment.objects.filter(
        video=video,
        parent=None
    ).select_related('user').prefetch_related('replies__user')
    
    return render(request, 'comments/comments_section.html', {
        'comments': comments,
        'video': video
    })