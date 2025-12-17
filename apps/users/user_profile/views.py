from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AvatarUploadForm
from .models import UserProfile

@login_required
def profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    form = AvatarUploadForm(instance=profile)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def upload_avatar(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avatar uploaded successfully.')
            return redirect('user_profile:profile') 
    else:
        form = AvatarUploadForm(instance=profile)
    return render(request, 'upload.html', {'form': form})