from django.urls import path
from .views import profile_view, upload_avatar

app_name = 'user_profile'

urlpatterns = [
    path('', profile_view, name='profile'),        # /users/profile/
    path('upload/', upload_avatar, name='upload')  # /users/profile/upload/
]
