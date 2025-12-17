from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SubscriptionPlan, UserSubscription
from apps.users.user_profile.models import UserProfile
from apps.users.models import CustomerUser  # Make sure this points to your custom user model
from apps.videos.models import Video  # Your Video model

# List all subscription plans
def plans_list(request):
    plans = SubscriptionPlan.objects.all()
    return render(request, 'subscriptions/plans.html', {'plans': plans})

# Subscribe user to a plan
@login_required
def subscribe(request, plan_id):
    plan = SubscriptionPlan.objects.get(id=plan_id)
    sub, _ = UserSubscription.objects.get_or_create(user=request.user)
    sub.plan = plan
    sub.active = True
    sub.save()

    # Reflect on profile for quick checks
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    profile.is_subscribed = True
    profile.save()

    messages.success(request, f'Subscribed to {plan.name}.')
    return redirect('user_profile:profile')


# View a user's channel and their videos
def channel_view(request, user_id):
    # Get the user whose channel is being visited
    user = get_object_or_404(CustomerUser, id=user_id)
    
    # Fetch videos uploaded by this user
    videos = Video.objects.filter(uploader=user)
    
    context = {
        'channel_user': user,
        'videos': videos,
    }
    return render(request, 'subscriptions/channel.html', context)
