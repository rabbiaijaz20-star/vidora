from django.db import models
from django.conf import settings


def avatar_upload_path(instance, filename):
    return f'avatars/user_{instance.user_id}/{filename}'

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to=avatar_upload_path, blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True)
    is_subscribed = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Profile({self.user.username})'