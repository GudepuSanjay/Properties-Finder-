from django.urls import path

from accounts import views
from buying_properties.views import buying_properties
urlpatterns = [
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/update/user',views.update_profile_user,name='update_profile_user'),
    path('profile/update/agent',views.update_profile_agent,name='update_profile_agent'),



    path('agent_dashboard/',views.agent_dashboard,name='agent_dashboard'),
    path('user_dashboard/',views.user_dashboard,name='user_dashboard'),
    
   
 
]
