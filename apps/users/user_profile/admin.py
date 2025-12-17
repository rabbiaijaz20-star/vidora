from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'avatar', 'is_subscribed', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('is_subscribed', 'created_at') 