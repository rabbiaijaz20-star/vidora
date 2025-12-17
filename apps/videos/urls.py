from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
    path('', views.video_list, name='list'),
    path('upload/', views.upload_video, name='upload'),
    path('watch/<int:video_id>/', views.watch_video, name='watch'),   # FIXED
    path('my-videos/', views.my_videos, name='my_videos'),
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),
]
