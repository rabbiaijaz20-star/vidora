from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# -----------------------------------------------------
# Custom User Model (Your custom name: CustomerUser)
# -----------------------------------------------------


class CustomerUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.username

# -----------------------------------------------------
# User Profile Model (Extra information)
# -----------------------------------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# -----------------------------------------------------
# Subscription System
# -----------------------------------------------------
class Subscription(models.Model):
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='subscribing',
        on_delete=models.CASCADE
    )
    subscribed_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='subscribers',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('subscriber', 'subscribed_to')

    def __str__(self):
        return f"{self.subscriber} → {self.subscribed_to}"
