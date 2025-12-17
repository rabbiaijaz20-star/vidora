from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser, Subscription
from apps.users.user_profile.models import UserProfile


class CustomerUserAdmin(UserAdmin):
    model = CustomerUser
    list_display = ('username', 'email', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('profile_picture', 'bio')}),
    )

admin.site.register(CustomerUser, UserAdmin)
admin.site.register(Subscription)
