from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from apps.users.signup_forms.views import SignUpView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

    # Include the user_profile URLs
    path('profile/', include('apps.users.user_profile.urls')),  # /users/profile/...
]
