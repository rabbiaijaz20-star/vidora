from django.urls import path, include
from .views import toggle_like
from . import views

app_name = 'likes'

urlpatterns = [
    path('toggle/<int:video_id>/', views.toggle_like, name='toggle_like'),
    path('my-liked-videos/', views.liked_videos, name='liked_videos'),
    
]
