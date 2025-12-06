from django.db import models
from django.conf import settings

class Comment(models.Model):
    video = models.ForeignKey(
        'videos.Video',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['video', '-created_at']),
        ]

    def __str__(self):
        return f"{self.user.username} on {self.video.title}"

    def get_replies(self):
        return self.replies.all().select_related('user')