from django.urls import path

from properties_bookings import views
# from agents_profiles import views

urlpatterns = [
    # path('create_booking/',views.create_booking,name='create_booking'),
    path('book/<int:property_id>/',views.book_visit,name='book_visit'),
    path('my_bookings/',views.user_bookings,name='user_bookings'),
    path('appointments/',views.my_appointments,name='appointments'),
    path('appointments/update/<int:id>/', views.update_appointment_status, name='update_appointment_status'),
    path('my_bookings/cancel/<int:booking_id>',views.cancel_booking,name="cancel_booking")
    # path('appointments/<int:id>/', views.appointment_detail, name='appointment_detail'),
]



