from django.db import models
from django.conf import settings

class Subscription(models.Model):
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )
    channel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscribers'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    notifications_enabled = models.BooleanField(default=True)

    class Meta:
        unique_together = ('subscriber', 'channel')
        indexes = [
            models.Index(fields=['subscriber', 'channel']),
        ]

    def __str__(self):
        return f"{self.subscriber.username} → {self.channel.username}"

    @staticmethod
    def get_subscriber_count(user):
        return Subscription.objects.filter(channel=user).count()

    @staticmethod
    def is_subscribed(subscriber, channel):
        return Subscription.objects.filter(
            subscriber=subscriber,
            channel=channel
        ).exists()