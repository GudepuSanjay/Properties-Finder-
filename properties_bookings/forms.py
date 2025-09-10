from django import forms
from .models import Bookings

class BookingForm(forms.ModelForm):
    class Meta:
        model=Bookings
        fields=['visit_date','message']
        widgets={
            'visit_date':forms.DateInput(attrs={'type':'date'}),
            'message':forms.Textarea(attrs={'rows':3}),
        }
