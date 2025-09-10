from .models import Property
from django import forms

class PropertyForm(forms.ModelForm):
    class Meta:
        model=Property
        fields=['title','description','price','property_type','status','image','locations','bedrooms','bathrooms','squarefeets','type_property','amenities','zip_code','near_location']