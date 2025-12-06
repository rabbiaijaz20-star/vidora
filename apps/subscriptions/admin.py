from django.contrib import admin
from .models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'channel', 'notifications_enabled', 'created_at')
    list_filter = ('notifications_enabled', 'created_at')
    search_fields = ('subscriber__username', 'channel__username')
    date_hierarchy = 'created_at'