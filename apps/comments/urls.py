from django.urls import path
from . import views

app_name = 'comments'  # MUST match the tuple in project-level urls.py

urlpatterns = [
    path('add/<int:video_id>/', views.add_comment, name='add_comment'),
    path('delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('fetch/<int:video_id>/', views.get_comments, name='fetch_comments'),
]
