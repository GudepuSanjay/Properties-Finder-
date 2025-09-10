from django import urls
from django.urls import path
from profiles.views import user_profile,agent_profile
from profiles import views


urlpatterns = [
    path('user/profile',views.user_profile, name="user_profile"),
    path('agent/profile',views.agent_profile,name="agent_profile"),
]