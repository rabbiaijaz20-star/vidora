# apps/likes/models.py
from django.db import models
from apps.videos.models import Video
from apps.users.models import CustomerUser

class Like(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="video_likes")  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
