from django.urls import path
from .views import plans_list, subscribe, channel_view  # import everything needed

app_name = 'subscriptions'

urlpatterns = [
    path('', plans_list, name='subscription_plans'),
    path('subscribe/<int:plan_id>/', subscribe, name='subscribe'),
    path('channel/<int:user_id>/', channel_view, name='channel'),  # now works
]
