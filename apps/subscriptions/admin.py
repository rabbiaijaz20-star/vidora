from django.contrib import admin
from .models import SubscriptionPlan, UserSubscription   # ✅ match actual models

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'active')
    list_filter = ('active', 'plan')
    search_fields = ('user__username', 'plan__name')