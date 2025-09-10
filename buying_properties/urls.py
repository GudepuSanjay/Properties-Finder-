from django.urls import path 
from . import views

urlpatterns = [
    path('user_dashboard/buy/',views.buying_properties,name="buy_properties"),
]


