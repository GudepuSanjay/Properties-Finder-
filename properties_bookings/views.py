from django.shortcuts import render
from properties.models import Property
from django.shortcuts import render, redirect,get_object_or_404
from properties_bookings.forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from properties_bookings.models import Bookings
# Create your views here.
@login_required
def book_visit(request,property_id):
    property_obj=get_object_or_404(Property,id=property_id)
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            booking=form.save(commit=False)
            booking.user=request.user
            booking.property=property_obj
            booking.save()
            return redirect('user_bookings')
    else:
        form=BookingForm()
    return render(request,'bookings/book_visit.html',{'form':form,'property':property_obj})

@login_required
def user_bookings(request):
    bookings=Bookings.objects.filter(user=request.user).select_related('property')
    return render(request,'bookings/user_bookings.html',{'bookings':bookings})

@login_required
def my_appointments(request):
    apponitments=Bookings.objects.filter(user=request.user)
    return render(request,'bookings/my_appointments.html',{'appointments':apponitments})

@login_required
def cancel_booking(request, booking_id):
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        booking = get_object_or_404(Bookings, id=booking_id, user=request.user)

        if booking.status in ["Pending", "Confirmed"]:
            booking.status = "Cancelled"
            booking.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "This booking cannot be cancelled."})
    
    return JsonResponse({"success": False, "error": "Invalid request."})



@login_required
def update_appointment_status(request, id):
    appointment = get_object_or_404(Bookings, id=id)

    if request.method == "POST":
        status = request.POST.get("status")
        if status in ["Pending", "Confirmed", "Cancelled"]:
            appointment.status = "Accepted" if status == "Confirmed" else status
            appointment.save()
            messages.success(request, f"Appointment status updated to {appointment.status}")
    return redirect(request.META.get('HTTP_REFERER', 'my_appointments'))

