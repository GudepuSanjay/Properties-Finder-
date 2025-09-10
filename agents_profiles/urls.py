from django.urls import path
from agents_profiles import views
urlpatterns = [
   path('user_dashboard/agents',views.agents_profiles,name="agents_profiles"),
]
