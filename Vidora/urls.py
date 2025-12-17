from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.users.views import home  # project-level home view



urlpatterns = [
    path('admin/', admin.site.urls),

    # Project-level home page
    path('', home, name='home'),

    # Users
    path('users/', include(('apps.users.urls', 'users'), namespace='users')),  # login, logout, signup
    path('users/profile/', include(('apps.users.user_profile.urls', 'user_profile'), namespace='user_profile')),
    
    path('videos/', include(('apps.videos.urls', 'videos'), namespace='videos')),

    # Likes
    path('likes/', include(('apps.likes.urls', 'likes'), namespace='likes')),

    # Comments
    path('comments/', include(('apps.comments.urls', 'comments'), namespace='comments')),

    # Subscriptions
    path('subscriptions/', include(('apps.subscriptions.urls', 'subscriptions'), namespace='subscriptions')),

    # Django built-in auth
    path('accounts/', include('django.contrib.auth.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
