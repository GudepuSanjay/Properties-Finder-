from django.urls import path
from rent_properties import views


urlpatterns = [
     path('user_dashboard/rent',views.rent_properties,name="rent_properties"),
]
