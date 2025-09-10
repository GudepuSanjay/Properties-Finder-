from django.urls import path

from . import views

urlpatterns = [
    path('properties/',views.property_list,name='property_list'),
    path('property/<int:pk>/',views.property_detail,name='property_detail'),
    path('agent/properties/',views.agent_property_list,name='agent_property_list'),
    path('agent/add-property/',views.add_property,name='add_property'),
    path('agent/agent_dashboard/properties/',views.agent_property_list,name='agent_property_list'),
]
