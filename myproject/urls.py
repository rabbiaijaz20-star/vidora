from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),  # This connects your users URLs
    path('', include('apps.videos.urls')),       # Home page is videos list
]
