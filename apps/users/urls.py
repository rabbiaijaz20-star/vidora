from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='users_home'),            # /users/
    path('login/', views.login_view, name='redirect_login'),    # /users/login/
    path('signup/', views.signup_view, name='redirect_signup'), # /users/signup/
    path('profile/', views.profile, name='redirect_profile'),   # /users/profile/
]
