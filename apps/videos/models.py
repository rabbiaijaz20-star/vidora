from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

class Video(models.Model):
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='videos'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(
        upload_to='videos/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])]
    )
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    views_count = models.PositiveIntegerField(default=0)
    duration = models.DurationField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ['-uploaded_at']
        indexes = [
            models.Index(fields=['-uploaded_at']),
            models.Index(fields=['uploader']),
        ]

    def __str__(self):
        return self.title

    def get_likes_count(self):
        return self.likes.count()

    def get_comments_count(self):
        return self.comments.count()

    def increment_views(self):
        self.views_count += 1
        self.save(update_fields=['views_count'])