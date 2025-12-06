from django.db import models
from django.conf import settings

class Like(models.Model):
    video = models.ForeignKey(
        'videos.Video',
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='liked_videos'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('video', 'user')
        indexes = [
            models.Index(fields=['video', 'user']),
        ]

    def __str__(self):
        return f"{self.user.username} likes {self.video.title}"