from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from .models import Subscription
from apps.videos.models import Video

@login_required
@require_POST
def toggle_subscription(request, user_id):
    channel = get_object_or_404(settings.AUTH_USER_MODEL, id=user_id)
    
    # Can't subscribe to yourself
    if channel == request.user:
        return JsonResponse({
            'success': False,
            'error': 'Cannot subscribe to yourself'
        }, status=400)
    
    subscription, created = Subscription.objects.get_or_create(
        subscriber=request.user,
        channel=channel
    )
    
    if not created:
        subscription.delete()
        subscribed = False
    else:
        subscribed = True
    
    subscriber_count = Subscription.get_subscriber_count(channel)
    
    return JsonResponse({
        'success': True,
        'subscribed': subscribed,
        'subscriber_count': subscriber_count
    })

@login_required
def my_subscriptions(request):
    subscriptions = Subscription.objects.filter(
        subscriber=request.user
    ).select_related('channel')
    
    channels = [sub.channel for sub in subscriptions]
    
    return render(request, 'subscriptions/my_subscriptions.html', {
        'channels': channels
    })

@login_required
def subscription_feed(request):
    # Get all channels user is subscribed to
    subscribed_channels = Subscription.objects.filter(
        subscriber=request.user
    ).values_list('channel', flat=True)
    
    # Get videos from subscribed channels
    videos = Video.objects.filter(
        uploader__in=subscribed_channels,
        is_public=True
    ).select_related('uploader').order_by('-uploaded_at')
    
    from django.core.paginator import Paginator
    paginator = Paginator(videos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'subscriptions/feed.html', {'page_obj': page_obj})

def channel_view(request, user_id):
    channel = get_object_or_404(settings.AUTH_USER_MODEL, id=user_id)
    videos = Video.objects.filter(
        uploader=channel,
        is_public=True
    ).order_by('-uploaded_at')
    
    subscriber_count = Subscription.get_subscriber_count(channel)
    is_subscribed = False
    
    if request.user.is_authenticated:
        is_subscribed = Subscription.is_subscribed(request.user, channel)
    
    from django.core.paginator import Paginator
    paginator = Paginator(videos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'subscriptions/channel.html', {
        'channel': channel,
        'page_obj': page_obj,
        'subscriber_count': subscriber_count,
        'is_subscribed': is_subscribed,
    })