from django.urls import path
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('toggle/<int:user_id>/', views.toggle_subscription, name='toggle'),
    path('my-subscriptions/', views.my_subscriptions, name='my_subscriptions'),
    path('feed/', views.subscription_feed, name='feed'),
    path('channel/<int:user_id>/', views.channel_view, name='channel'),
]