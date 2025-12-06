from django.urls import path
from . import views

app_name = 'likes'

urlpatterns = [
    path('toggle/<int:video_id>/', views.toggle_like, name='toggle'),
    path('my-likes/', views.liked_videos, name='my_likes'),
]